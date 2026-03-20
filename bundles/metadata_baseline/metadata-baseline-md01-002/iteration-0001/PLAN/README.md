## MD-01 Plan

Loop instance: `metadata-baseline-md01-002`  
Iteration: `iteration-0001`

### Scope

Execute the first stackable micro-deliverable from the merged release plan:

- `MD-01`: workspace probe

### Objective

Prove the known-good Codex workspace shape with the smallest possible validation:

- resolve the authoritative Cargo workspace manifest
- resolve the authoritative workspace root
- emit stable probe outputs for downstream use

### Target

- repo root: `/home/_404/src/repo_intel/codex`
- expected workspace manifest: `/home/_404/src/repo_intel/codex/codex-rs/Cargo.toml`
- expected workspace root: `/home/_404/src/repo_intel/codex/codex-rs`

### Validation bar

- `just test-md01-workspace-probe` passes
- `just ci` passes
- emitted probe matches the expected workspace manifest/root exactly

### Follow-on

Next micro-deliverable after this batch:

- `MD-02`: dual metadata capture
