## MD-04 Plan

Loop instance: `metadata-baseline-md04-005`  
Iteration: `iteration-0001`

### Scope

Execute the refreshed edge-table slice:

- `MD-04`: package dependency edge table and edge summary

### Objective

Derive a stable edge table from the accepted metadata pair and expose the
latest cross-crate dependency structure for the promoted Codex pilot assets.

### Validation bar

- `package-edges.tsv` is emitted
- `edge-summary.json` is emitted
- edges for `codex-app-server`, `codex-exec-server`, and `codex-login` are
  derivable from the current local snapshot
- missing promoted crates are surfaced explicitly rather than guessed into
  existence
- `Cargo.lock` freshness input is recorded
- `just test-md04-edge-table` exits `0`
- `just ci-md04` exits `0`

### Follow-on

Next micro-deliverable after this batch:

- `MD-06`: protocol/plugin/execution drift report
