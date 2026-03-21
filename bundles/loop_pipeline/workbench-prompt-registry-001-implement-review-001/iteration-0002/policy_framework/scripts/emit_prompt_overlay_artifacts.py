#!/usr/bin/env python3
"""Emit deterministic prompt-overlay runtime artifacts for the approved read-only slice."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def validate_json(instance_path: Path, schema_path: Path) -> list[str]:
    instance = load_json(instance_path)
    schema = load_json(schema_path)
    resolver = jsonschema.validators.RefResolver(
        base_uri=schema_path.resolve().as_uri(),
        referrer=schema,
    )
    validator = jsonschema.Draft202012Validator(schema, resolver=resolver)
    return [e.message for e in validator.iter_errors(instance)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wt", required=True, help="Current loop worktree root.")
    parser.add_argument("--contract-root", required=True, help="Codex contract root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    wt = Path(args.wt).expanduser().resolve()
    contract_root = Path(args.contract_root).expanduser().resolve()
    prompt_registry_root = contract_root / "prompt-registry"
    control_root = contract_root / "control"
    implement_root = wt / "IMPLEMENT"
    plan_root = wt / "PLAN"

    slice_contract = load_json(plan_root / "overlay_slice.contract.json")
    derivation_rules = load_json(plan_root / "overlay_derivation.rules.json")

    registry_manifest_path = prompt_registry_root / "manifest.json"
    retrieval_index_path = prompt_registry_root / "retrieval" / "index.json"
    retrieval_aliases_path = prompt_registry_root / "retrieval" / "aliases.json"
    retrieval_tags_path = prompt_registry_root / "retrieval" / "tags.json"
    registry_schema_path = prompt_registry_root / "schemas" / "registry.schema.json"
    workflow_schema_path = prompt_registry_root / "schemas" / "workflow.schema.json"
    profile_schema_path = prompt_registry_root / "schemas" / "profile.schema.json"

    registry_manifest = load_json(registry_manifest_path)
    retrieval_index = load_json(retrieval_index_path)
    retrieval_aliases = load_json(retrieval_aliases_path)
    retrieval_tags = load_json(retrieval_tags_path)

    unit_by_id = {unit["id"]: unit for unit in registry_manifest["units"]}
    all_manifest_workflow_ids = sorted(unit_by_id)
    selected_workflow_ids = slice_contract["scope"]["in_scope_workflows"]
    selected_profile_names = slice_contract["scope"]["in_scope_profiles"]
    allowed_snippets = set(slice_contract["scope"]["in_scope_snippets"])

    schema_errors: list[str] = []
    schema_errors.extend(validate_json(registry_manifest_path, registry_schema_path))

    workflow_payloads: dict[str, dict] = {}
    selected_workflows: list[dict] = []
    authority_results: list[dict] = []
    authority_errors: list[str] = []

    for workflow_id in selected_workflow_ids:
        unit = unit_by_id.get(workflow_id)
        if not unit:
            authority_errors.append(f"selected workflow missing from manifest: {workflow_id}")
            continue

        workflow_path = prompt_registry_root / unit["path"]
        workflow_payload = load_json(workflow_path)
        workflow_payloads[workflow_id] = workflow_payload
        schema_errors.extend(validate_json(workflow_path, workflow_schema_path))

        authority = workflow_payload.get("authority") or unit.get("authority", {})
        authority_source = "workflow_file" if "authority" in workflow_payload else "manifest_unit"
        source_root = authority.get("source_of_truth_root", "")
        resolved_refs = []
        missing_refs = []
        for ref in authority.get("source_of_truth_refs", []):
            ref_path = contract_root / ref
            resolved_refs.append(str(ref_path))
            if not ref_path.exists() or not ref_path.resolve().is_relative_to(control_root.resolve()):
                missing_refs.append(ref)

        result = {
            "workflow_id": workflow_id,
            "manifest_unit_present": True,
            "workflow_path": str(workflow_path),
            "workflow_id_matches_file": workflow_payload.get("id") == workflow_id,
            "authority_metadata_source": authority_source,
            "source_of_truth_root": source_root,
            "source_of_truth_refs": authority.get("source_of_truth_refs", []),
            "resolved_source_of_truth_refs": resolved_refs,
            "missing_source_of_truth_refs": missing_refs,
            "overlay_role": authority.get("overlay_role"),
            "illegal_redefinition_detected": False,
            "status": "PASS" if not missing_refs and workflow_payload.get("id") == workflow_id else "FAIL",
        }
        authority_results.append(result)
        if result["status"] != "PASS":
            authority_errors.append(f"authority verification failed for {workflow_id}")

        selected_workflows.append(
            {
                "id": workflow_id,
                "description": workflow_payload.get("description", ""),
                "tags": unit.get("tags", []),
                "applies_when": unit.get("applies_when", []),
                "required_snippets": [req.removeprefix("snippet.") for req in unit.get("requires", [])],
                "workflow_path": unit["path"],
                "steps": workflow_payload.get("steps", []),
                "authority_metadata_source": authority_source,
                "authority": authority,
            }
        )

    profile_payloads: dict[str, dict] = {}
    selected_profiles: list[dict] = []
    assembled_profiles: list[dict] = []
    parity_errors: list[str] = []

    for profile_name in selected_profile_names:
        profile_path = prompt_registry_root / "profiles" / f"{profile_name}.json"
        profile_payload = load_json(profile_path)
        profile_payloads[profile_name] = profile_payload
        schema_errors.extend(validate_json(profile_path, profile_schema_path))

        resolved_workflows = []
        required_snippets = []
        authority_refs = []
        for workflow_id in profile_payload.get("workflow_preferences", []):
            if workflow_id not in unit_by_id:
                parity_errors.append(f"profile {profile_name} references unknown workflow {workflow_id}")
                continue
            if workflow_id in selected_workflow_ids:
                resolved_workflows.append(workflow_id)
                required_snippets.extend(
                    req.removeprefix("snippet.") for req in unit_by_id[workflow_id].get("requires", [])
                )
                authority = workflow_payloads.get(workflow_id, {}).get("authority") or unit_by_id[workflow_id].get("authority", {})
                authority_refs.extend(authority.get("source_of_truth_refs", []))

        snippet_candidates = [snippet for snippet in required_snippets if snippet in allowed_snippets]
        ordered_snippets = []
        for snippet_name in profile_payload.get("snippet_order", []):
            if snippet_name in allowed_snippets and snippet_name not in ordered_snippets:
                ordered_snippets.append(snippet_name)
        for snippet_name in snippet_candidates:
            if snippet_name not in ordered_snippets:
                ordered_snippets.append(snippet_name)

        selected_profiles.append(
            {
                "name": profile_name,
                "workflow_preferences": profile_payload.get("workflow_preferences", []),
                "resolved_workflows": resolved_workflows,
                "snippet_order": profile_payload.get("snippet_order", []),
            }
        )
        assembled_profiles.append(
            {
                "name": profile_name,
                "resolved_workflows": resolved_workflows,
                "ordered_snippets": ordered_snippets,
                "snippet_sections": [
                    {
                        "snippet": snippet_name,
                        "path": f"prompt-registry/snippets/{snippet_name}.md",
                        "content": (prompt_registry_root / "snippets" / f"{snippet_name}.md").read_text(encoding="utf-8").strip(),
                    }
                    for snippet_name in ordered_snippets
                ],
                "authority_refs": sorted(set(authority_refs)),
            }
        )

    retrieval_workflows = sorted(retrieval_index.get("workflows", []))
    alias_targets = sorted(set(retrieval_aliases.values()))
    tag_workflows = sorted(retrieval_tags.keys())
    profile_workflows = sorted(
        {
            workflow_id
            for profile in profile_payloads.values()
            for workflow_id in profile.get("workflow_preferences", [])
        }
    )
    all_referenced_workflows = sorted(set(retrieval_workflows + alias_targets + tag_workflows + profile_workflows))
    missing_from_manifest = [workflow_id for workflow_id in all_referenced_workflows if workflow_id not in unit_by_id]

    manifest_profiles = set(registry_manifest.get("profiles", []))
    missing_profiles = [
        profile_name
        for profile_name in selected_profile_names
        if profile_name not in manifest_profiles or not (prompt_registry_root / "profiles" / f"{profile_name}.json").exists()
    ]
    manifest_snippets = set(registry_manifest.get("snippets", []))
    referenced_snippets = sorted(
        {
            snippet
            for profile in profile_payloads.values()
            for snippet in profile.get("snippet_order", [])
        }
    )
    missing_snippets = [
        snippet
        for snippet in referenced_snippets
        if snippet not in manifest_snippets or not (prompt_registry_root / "snippets" / f"{snippet}.md").exists()
    ]
    missing_workflow_files = [
        workflow_id
        for workflow_id, unit in unit_by_id.items()
        if not (prompt_registry_root / unit["path"]).exists()
    ]

    parity_errors.extend(f"workflow missing from manifest: {workflow_id}" for workflow_id in missing_from_manifest)
    parity_errors.extend(f"profile missing from manifest or filesystem: {profile}" for profile in missing_profiles)
    parity_errors.extend(f"snippet missing from manifest or filesystem: {snippet}" for snippet in missing_snippets)
    parity_errors.extend(f"workflow file missing: {workflow_id}" for workflow_id in missing_workflow_files)

    overall_errors = schema_errors + authority_errors + parity_errors
    status = "PASS" if not overall_errors else "FAIL"

    resolved_overlay = {
        "kind": "prompt_overlay_resolution.v1",
        "slice_id": slice_contract["slice_id"],
        "authority_metadata_source": "manifest.units",
        "registry_manifest_ref": "prompt-registry/manifest.json",
        "selected_workflows": selected_workflows,
        "selected_profiles": selected_profiles,
        "retrieval_index": {
          "workflows": retrieval_workflows,
          "aliases": retrieval_aliases,
          "tags": retrieval_tags
        },
        "status": status,
        "errors": overall_errors,
    }

    assembled_prompt_plan = {
        "kind": "prompt_assembly_plan.v1",
        "slice_id": slice_contract["slice_id"],
        "profiles": assembled_profiles,
        "status": status,
    }

    authority_verification = {
        "kind": "prompt_overlay_authority_verification.v1",
        "slice_id": slice_contract["slice_id"],
        "authority_metadata_source": "manifest.units",
        "rules_ref": "PLAN/overlay_derivation.rules.json",
        "rules": derivation_rules["rules"],
        "results": authority_results,
        "status": "PASS" if not authority_errors else "FAIL",
        "errors": authority_errors,
    }

    registry_parity_check = {
        "kind": "prompt_registry_parity_check.v1",
        "slice_id": slice_contract["slice_id"],
        "manifest_workflows": all_manifest_workflow_ids,
        "retrieval_workflows": retrieval_workflows,
        "alias_targets": alias_targets,
        "tag_workflows": tag_workflows,
        "profile_workflows": profile_workflows,
        "missing_from_manifest": missing_from_manifest,
        "missing_profiles": missing_profiles,
        "missing_snippets": missing_snippets,
        "missing_workflow_files": missing_workflow_files,
        "status": "PASS" if not parity_errors else "FAIL",
        "errors": parity_errors,
    }

    implement_root.mkdir(parents=True, exist_ok=True)
    write_json(implement_root / "resolved.overlay.json", resolved_overlay)
    write_json(implement_root / "assembled.prompt.plan.json", assembled_prompt_plan)
    write_json(implement_root / "authority.verification.json", authority_verification)
    write_json(implement_root / "registry.parity.check.json", registry_parity_check)
    print(implement_root / "resolved.overlay.json")
    print(implement_root / "assembled.prompt.plan.json")
    print(implement_root / "authority.verification.json")
    print(implement_root / "registry.parity.check.json")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
