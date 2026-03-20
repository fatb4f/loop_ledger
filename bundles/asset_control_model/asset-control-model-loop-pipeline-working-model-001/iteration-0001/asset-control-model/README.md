## Asset Control Model

Workbench path: `/home/_404/src/workbench/asset-control-model`

### Role

Active project surface for the policy-plane and contract-first delivery model.

### Current linked source

- source repo: [asset-control-model](/home/_404/src/runtime/asset-control-model)
- current promoted head: `c68d364`

### Current state

The source repo now has:

- a real Git source root
- contract-branch and integration-worktree execution already exercised
- a promoted initial implementation under [policy_framework](/home/_404/src/runtime/asset-control-model/policy_framework)

Verified behaviors already exist for:

- `cargo check --workspace`
- `cargo metadata --no-deps`
- `just validate`
- `just reconcile`
- `bash scripts/policy_ci.sh`

### Near-term implementation focus

- define the gating and promotion contract that offloaded metadata work must satisfy
- replace placeholder JSON Schema files with real schemas
- strengthen CUE admissibility rules
- finish typed promotion and gate evidence surfaces
- align ACM policy surfaces with the shared Codex git-flow control layer

### Working model for loop-pipeline contracts

The current loop pipeline needs a frozen minimal ACM surface before broader ACM
generalization.

See:

- [loop_pipeline_working_model.md](/home/_404/src/runtime/asset-control-model/policy_framework/policy/loop_pipeline_working_model.md)
- [loop_pipeline_working_model.v1.json](/home/_404/src/runtime/asset-control-model/policy_framework/policy/loop_pipeline_working_model.v1.json)
