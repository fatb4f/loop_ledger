## MD-02 Plan

Loop instance: `metadata-baseline-md02-003`  
Iteration: `iteration-0001`

### Scope

Execute the next stackable micro-deliverable from the refreshed Codex pilot:

- `MD-02`: raw metadata pair

### Objective

Prove the structural truth source for the refreshed Codex pilot by emitting:

- `metadata.workspace.json`
- `metadata.host.json`

with machine-checkable evidence for both Cargo metadata commands and the wrapped
validation steps.

### Target

- repo root: `/home/_404/src/repo_intel/codex`
- workspace root: `/home/_404/src/repo_intel/codex/codex-rs`
- pilot surface: `post320_surface`

### Validation bar

- `cargo metadata --no-deps` exits `0`
- `cargo metadata` exits `0`
- `just test-md02-metadata-pair` exits `0`
- `just ci-md02` exits `0`
- workspace metadata contains `workspace_members` and `packages`
- host metadata contains `resolve.nodes`

### Follow-on

Next micro-deliverable after this batch:

- `MD-03`: refreshed pilot package census
