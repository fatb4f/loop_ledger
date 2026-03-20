## MD-03 Plan

Loop instance: `metadata-baseline-md03-004`  
Iteration: `iteration-0001`

### Scope

Execute the refreshed pilot package census:

- `MD-03`: package census and workspace summary

### Objective

Derive a stable package inventory from the accepted MD-02 metadata pair and
record which promoted pilot crates are present or missing in the current local
Codex snapshot.

### Validation bar

- `packages.tsv` is emitted
- `workspace-summary.json` is emitted
- workspace package count equals workspace member count
- promoted crates present in the current snapshot are recorded correctly
- absent promoted crates are surfaced explicitly, not guessed into existence
- `just test-md03-package-census` exits `0`
- `just ci-md03` exits `0`

### Follow-on

Next micro-deliverable after this batch:

- `MD-04`: refreshed edge table
