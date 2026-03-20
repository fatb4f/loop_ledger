# Policy Framework Skeleton

This directory is the first concrete micro-deliverable for the policy-plane design.

It turns the framework in [policy_framework.md](/home/_404/src/codex/back_to_code/policy_framework/policy_framework.md)
into a minimal runnable skeleton with:

- a Cargo workspace for policy binaries and libraries
- a `just` operator surface above Cargo
- example workspace/controller records
- explicit separation between schemas, policy, manifests, and events

## Authority split

- Cargo owns Rust execution and workspace/package truth.
- `just` owns the operator-facing command surface.
- JSON Schema owns JSON boundary validation.
- CUE owns cross-document invariants and derivation.
- jq is the read-only observer layer.

## First iteration

This skeleton is intentionally small. It proves the control-plane shape without trying
to implement a full policy engine in one batch.

### Included crates

- `policy-manifest`: shared manifest and workspace-record types
- `policy-events`: handoff and event-log types
- `policy-validate`: boundary validation entrypoint
- `policy-reconcile`: reconciliation entrypoint
- `cargo-policy`: future Cargo subcommand surface

### Included command surface

- `just validate`
- `just reconcile`
- `just audit`
- `just doctor`
- `just metadata`
- `just promote-plan`

### Included records

- `workspaces/asset-control-model.toml`: example workspace controller record

### Contract-layer layout added on the contract branch

- `policy/control_plane.cue`: initial CUE package boundary for cross-document policy
- `scripts/policy_ci.sh`: deterministic CI wrapper for workspace verification
- `just ci`: stable operator entrypoint for CI checks

## Next batch

- replace stub CLI behavior with real validators and reconcilers
- add JSON Schema documents under `schemas/`
- extend the initial CUE policy package under `policy/`
- teach `cargo-policy` to resolve workspace handles into real `Cargo.toml` files

## Loop-pipeline working model

Before broadening ACM scope, the current loop pipeline should harden against
the minimal contract model captured in:

- [policy/loop_pipeline_working_model.md](/home/_404/src/runtime/asset-control-model/policy_framework/policy/loop_pipeline_working_model.md)
- [policy/loop_pipeline_working_model.v1.json](/home/_404/src/runtime/asset-control-model/policy_framework/policy/loop_pipeline_working_model.v1.json)

That model freezes the current packet, evidence-bundle, review-bundle, loop
state, lineage, and git-flow promotion surfaces so hardening can proceed
without reopening architecture scope.
