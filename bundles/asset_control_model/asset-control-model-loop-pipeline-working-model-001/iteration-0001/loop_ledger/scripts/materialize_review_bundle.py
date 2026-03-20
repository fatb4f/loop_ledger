#!/usr/bin/env python3
"""Materialize a review bundle from a manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, help="Path to review bundle manifest")
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_item(output_root: Path, item: dict) -> dict:
    source = Path(item["source"]).resolve()
    if not source.is_file():
        raise SystemExit(f"missing required bundle input: {source}")
    dest = output_root / item["dest"]
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)
    record = {
        "path": str(dest),
        "source": str(source),
        "role": item["role"],
        "repo_key": item["repo_key"],
        "repo_relative_path": item["repo_relative_path"],
        "head": item["head"],
        "sha256": sha256_file(dest),
    }
    if "absolute_path" in item:
        record["absolute_path"] = item["absolute_path"]
    if "name" in item:
        record["name"] = item["name"]
    return record


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    output_root = Path(manifest["output_root"]).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    files = []
    copied_roles: set[str] = set()
    for item in manifest["include"]:
        record = copy_item(output_root, item)
        files.append(record)
        copied_roles.add(record["role"])

    evidence_bundle = manifest["evidence_bundle"]
    for item in evidence_bundle["required_outputs"]:
        record = copy_item(output_root, item)
        files.append(record)
        copied_roles.add(record["role"])

    for item in evidence_bundle["required_checks"]:
        record = copy_item(output_root, item)
        files.append(record)
        copied_roles.add(record["role"])

    ref_header = {
        "kind": "review_bundle_ref_header.v1",
        "project": manifest["project"],
        "bundle_id": manifest["bundle_id"],
        "iteration_id": manifest["iteration_id"],
        "scope_root": manifest["scope_root"],
        "reviewed_head": manifest.get("reviewed_head", ""),
        "lineage": manifest.get("lineage", {}),
        "refs": manifest.get("refs", {}),
        "source_roots": manifest.get("source_roots", {}),
        "controller_surfaces": manifest.get("controller_surfaces", {}),
        "evidence_bundle": {
            "integrity_mode": evidence_bundle["integrity_mode"],
            "required_output_roles": [item["role"] for item in evidence_bundle["required_outputs"]],
            "required_check_roles": [item["role"] for item in evidence_bundle["required_checks"]],
        },
    }

    ref_header_path = output_root / "ref_header.json"
    ref_header_path.write_text(json.dumps(ref_header, indent=2) + "\n", encoding="utf-8")
    files.append(
        {
            "path": str(ref_header_path),
            "source": str(manifest_path),
            "role": "ref_header",
            "sha256": sha256_file(ref_header_path),
        }
    )

    bundle_manifest = {
        "kind": "review_bundle_artifacts_manifest.v1",
        "project": manifest["project"],
        "bundle_id": manifest["bundle_id"],
        "iteration_id": manifest["iteration_id"],
        "manifest_path": str(manifest_path),
        "output_root": str(output_root),
        "lineage": manifest.get("lineage", {}),
        "source_roots": manifest.get("source_roots", {}),
        "controller_surfaces": manifest.get("controller_surfaces", {}),
        "integrity_mode": evidence_bundle["integrity_mode"],
        "evidence_bundle": {
            "required_output_roles": [item["role"] for item in evidence_bundle["required_outputs"]],
            "required_check_roles": [item["role"] for item in evidence_bundle["required_checks"]],
        },
        "files": files,
    }

    manifest_out = output_root / "artifacts.manifest.json"
    manifest_out.write_text(json.dumps(bundle_manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest_out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
