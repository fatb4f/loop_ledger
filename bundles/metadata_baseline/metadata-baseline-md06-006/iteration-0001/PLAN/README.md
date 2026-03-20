## MD-06 Plan

Loop instance: `metadata-baseline-md06-006`  
Iteration: `iteration-0001`

### Scope

Execute the refreshed drift-report slice:

- `MD-06`: protocol/plugin/execution drift report

### Objective

Derive a stable set of drift reports from the accepted post320 surface and the
captured Codex delta extract, preserving the highest-signal protocol, plugin,
execution-boundary, and crate-split changes for analysis.

### Validation bar

- `asset-drift.app-server-protocol.json` is emitted
- `asset-drift.plugins.json` is emitted
- `asset-drift.exec-server.json` is emitted
- `asset-drift.crate-splits.json` is emitted
- app-server-protocol deletions in head are surfaced explicitly
- plugin lifecycle changes are rolled into a dedicated plugins asset
- exec-server keeps the local/remote/handler analysis tag
- codex-login and codex-features split status is recorded accurately
- `just test-md06-asset-drift` exits `0`
- `just ci-md06` exits `0`

### Follow-on

Next micro-deliverable after this batch:

- `MD-07`: refreshed asset-bucket summaries
