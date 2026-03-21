# Loop Pipeline Working Model

This document freezes the minimum Asset Control Model surface needed by the
current loop pipeline. It is intentionally narrower than the broader ACM draft.

## Purpose

Use this model for the existing loop pipeline so we can harden contract closure
without reopening architecture scope.

This working model applies to:

- loop/plan/implement packet handoff
- ledger-backed review bundle materialization
- evidence bundle gating
- lineage from parent planning bundle to derived implementation bundles
- git-flow promotion evidence for bounded batches
- controller surfaces that actuate those contracts:
  - scripts
  - manifests
  - schemas
  - `justfile`s

This working model does not yet attempt to generalize ACM across unrelated
asset families.

## Stable operating split

- `$wt`
  - source-repo integration worktree
  - owns `PLAN/*`, `IMPLEMENT/*`, and runtime-produced evidence
- `$ledger_wt`
  - `loop_ledger` worktree
  - owns review manifests, copied evidence, materialized bundles, and
    shareable archives

Do not overload these roles. Execution happens in `$wt`; copied review evidence
is curated in `$ledger_wt`.

## Controller surfaces in scope

The loop pipeline is not just packet JSON and copied artifacts. The controller
surface is also part of the frozen model.

Required controller surfaces:

- `justfile`s
  - operator entrypoints
  - stable public command surface
- scripts
  - narrow validators
  - packet generators
  - bundle materializers
- manifests
  - per-run declarations of expected artifacts and evidence
- schemas
  - machine-readable boundary validation for packets, manifests, and bundle
    metadata

These are in scope because they define admissible transitions and determine
whether a run can be validated, bundled, promoted, or denied.

## Tool authority for the current phase

The current implementation choice is:

- CUE
  - admissibility engine for workflow state
  - owns cross-document invariants over packets, bundles, lineage, provenance,
    and promotion state
- JSON Schema
  - boundary validation for individual JSON objects
- scripts
  - collect observed state
  - hash files
  - check file existence
  - invoke validation steps
  - materialize bundles
- `just`
  - operator-facing command surface over the scripts and schemas
- Cargo
  - workspace/package truth where Cargo-shaped projects are involved

A Rust controller binary is explicitly deferred. If introduced later, it should
consume this same contract surface rather than redefining it.

## Minimal control objects

The loop pipeline is frozen to six control-object classes.

### 1. Packet contract

Authority for the transition from `PLAN` to `IMPLEMENT` and from `IMPLEMENT` to
`VERIFY`.

Required surfaces:

- loop handoff contract
- plan request packet
- implement response packet
- contract bridge validation outputs

### 2. Loop state

Authority for the state-machine view of one loop iteration.

Required surface:

- one canonical loop-state artifact per iteration

Recommended artifact:

- `LOOP/loop.state.json`

Minimum fields:

- `loop_instance_id`
- `iteration_id`
- `phase`
- `previous_phase`
- `decision`
- `transition_gate`
- `verification_result`
- `rollback_status`
- `archive_ref`

### 3. Evidence bundle

Authority for what must exist before a review bundle can materialize.

Required surfaces:

- declared outputs
- declared check evidence
- integrity mode

Current implementation authority:

- `review_bundle_manifest.v1`
- `evidence_bundle.required_outputs`
- `evidence_bundle.required_checks`

### 4. Review bundle

Authority for the copied, review-facing proof object.

Required properties:

- self-contained enough to replay `VERIFY`
- hashed copied members
- explicit provenance per source root
- small by default, with copied evidence plus refs for deep provenance

### 5. Lineage and promotion capsule

Authority for derivation and git-flow promotion state.

Required surfaces:

- parent-plan lineage
- bounded-batch git-flow evidence

Recommended artifact:

- `gitflow/promotion.capsule.json`

Minimum fields:

- `integration_id`
- `base_main_commit`
- `contract_commit`
- `bounded_batch_id`
- `patch_hash`
- `validation_refs`
- `status`
- `promoted_commit` or `rejection_reason`

### 6. Controller surface

Authority for how the loop pipeline is invoked and validated.

Required surfaces:

- root or repo-local `justfile` operator surfaces
- validator and materializer scripts
- packet and bundle manifests
- packet and bundle schemas

Minimum required capabilities:

- validate packet artifacts
- validate bridge legality
- validate review-bundle manifests
- check required evidence presence
- materialize copied review bundles
- emit promotion or rejection evidence

## Plane mapping

### Policy plane

Defines what must remain true.

- CUE is the primary admissibility layer for workflow state.
- review generation denies on missing declared evidence
- promotion denies on failed bridge or failed validation
- downstream package-aware analysis denies on missing or stale handoff index
- every derived bundle must declare lineage to its parent plan bundle
- controller entrypoints must be thin wrappers over versioned scripts and
  schemas, not ad hoc shell logic

### Contract plane

Defines machine-readable shapes.

- loop handoff contract
- request/response packet schemas
- review bundle manifest schema
- evidence bundle declaration
- loop-state schema
- promotion capsule schema
- controller-facing manifest and validation schemas
- CUE policy packages that unify these shapes into admissibility checks

### Runtime plane

Defines observed artifacts.

- `PLAN/*`
- `IMPLEMENT/*`
- raw outputs
- check evidence
- loop-state artifact
- copied review bundle
- shareable review archive
- invoked scripts
- `justfile` entrypoints

## Validation flow

The current target flow is:

1. scripts collect observed packet, evidence, lineage, provenance, and
   promotion state into JSON
2. JSON Schema validates boundary objects
3. CUE evaluates cross-document admissibility
4. scripts translate the CUE verdict into `ALLOW`, `DENY`, `REPAIR`, or
   `PROMOTE`
5. `just` exposes the stable public entrypoints

This keeps the policy brain in CUE while leaving file operations and process
invocation to small controller scripts.

## Required closure for controller-grade review

The review of the current loop pipeline identified closure gaps. Treat the
following as the minimum hardening set.

### P0

- Make `VERIFY` replayable from the review bundle.
- Materialize loop state as a first-class artifact.
- Pin provenance per source root instead of relying on a single head value.

Minimum copied bridge for each review bundle:

- `PLAN/contract.bindings.json`
- `PLAN/request.validation.json`
- `PLAN/batch.manifest.json`
- `PLAN/integration_gate.plan.json`
- `PLAN/promotion.plan.json`
- `IMPLEMENT/response.manifest.json`
- `IMPLEMENT/response.validation.json`

### P1

- Gate the parent planning bundle with real required checks and evidence.
- Emit a canonical git-flow evidence capsule.
- Prefer repo-relative paths plus repo keys, with absolute paths only as
  optional convenience provenance.
- Scope controller scripts, manifests, schemas, and `justfile`s explicitly into
  provenance and review policy.

### P2

- Add authority-completeness validation so declared refs must resolve.
- Keep heavy outputs review-appropriate through policy rather than ad hoc
  judgment.

## Minimal provenance model

Review bundles should pin provenance per root, not by one generic
`reviewed_head`.

Recommended shape:

- `source_roots.codex`
- `source_roots.metadata_baseline`
- `source_roots.loop_ledger`

Controller provenance should also pin:

- `controller_surfaces.codex_skills`
- `controller_surfaces.metadata_baseline`
- `controller_surfaces.loop_ledger`

Each copied artifact should carry:

- `repo_key`
- `repo_relative_path`
- optional `absolute_path`
- `head`

## Scope guard

This working model is intentionally not a full ACM rollout.

Deferred:

- generalized `.control` bundles across unrelated projects
- full CUE policy expansion beyond loop-pipeline needs
- broad asset-family taxonomy work
- non-loop controller abstractions
- Rust controller binary replacement for the current script-based actuators

If a proposed change does not improve packet closure, evidence closure,
provenance closure, or promotion closure for the loop pipeline, it is out of
scope for this model.
