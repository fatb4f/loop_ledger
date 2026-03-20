## MD-07 Plan

Loop instance: `metadata-baseline-md07-007`  
Iteration: `iteration-0001`

### Scope

Execute the refreshed asset-summary slice:

- `MD-07`: refreshed asset-bucket summaries

### Objective

Turn the accepted post320 surface and accepted `MD-03` through `MD-06` outputs
into stable per-asset summaries aligned with the current Codex pilot reading
model.

### Validation bar

- ten asset summaries are emitted under `.analysis/reports/assets`
- each promoted asset gets a summary with commit rationale and ownership implications
- `core` remains the primary anchor but not the only authority bucket
- plugins remain a distinct asset bucket
- `codex-features` local absence remains explicit
- `just test-md07-asset-summaries` exits `0`
- `just ci-md07` exits `0`

### Follow-on

Next micro-deliverable after this batch:

- `MD-09`: freshness-aware handoff index
