# loop_ledger

Ledger repo for loop packets, review manifests, and materialized review bundles.

## Purpose

This repo is the process-evidence surface, not the implementation surface.

- implementation stays in source repos such as `/home/_404/src/repo_intel/metadata_baseline`
- curated planning/review inputs may live in workbench repos such as `/home/_404/src/workbench/metadata_baseline`
- `loop_ledger` stores normalized review manifests and reproducible copied bundles

## Operating model

```text
source repos -> review manifest -> bundle script -> materialized review bundle
```

The root [justfile](/home/_404/src/loop_ledger/justfile) is the controller surface.

## Controller commands

Generic:

- `just review-validate <manifest>`
- `just review-status <manifest>`
- `just review-materialize <manifest>`
- `just review-bundle <manifest>`

Seeded bundle:

- `just metadata-baseline-plan-merge-001-validate`
- `just metadata-baseline-plan-merge-001-status`
- `just metadata-baseline-plan-merge-001-bundle`
- `just metadata-baseline-md01-validate`
- `just metadata-baseline-md01-status`
- `just metadata-baseline-md01-bundle`

## Review gate

Review bundles are materialized from a manifest plus an explicit
`evidence_bundle` declaration.

The bundle step fails closed when:

- declared raw outputs are missing
- declared check evidence is missing
- required copied review artifacts are missing

This keeps review generation from overstating implementation strength.

## Initial seeded project

- `metadata_baseline`

The first seeded bundle is:

- `metadata-baseline-plan-merge-001`
- `metadata-baseline-md01-002`

All downstream `metadata_baseline` MD bundles should carry explicit lineage
back to the parent `metadata-baseline-plan-merge-001` manifest.
