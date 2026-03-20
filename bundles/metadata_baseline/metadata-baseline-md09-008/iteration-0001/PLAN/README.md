## MD-09 Plan

Loop instance: `metadata-baseline-md09-008`  
Iteration: `iteration-0001`

### Scope

Execute the freshness-aware handoff slice:

- `MD-09`: freshness-aware handoff index

### Objective

Emit a minimal production handoff index from the accepted metadata baseline
outputs so codex-web and just/scripts can consume one artifact-first surface
instead of a loose set of reports.

### Validation bar

- `.analysis/index.json` is emitted
- index records source head, Cargo.lock, and promoted crate set
- crate-set changes can mark the index stale
- downstream package-aware analysis can deny on stale or missing index
- `just test-md09-handoff-index` exits `0`
- `just ci-md09` exits `0`

### Closeout

This batch closes the current active post320 MD loop.
