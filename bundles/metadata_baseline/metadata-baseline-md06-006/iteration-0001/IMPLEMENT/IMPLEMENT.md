## MD-06 Implement

Loop instance: `metadata-baseline-md06-006`  
Iteration: `iteration-0001`

### Result

`MD-06` completed as a real drift-report slice derived from the accepted
post320 surface and the stored Codex delta extract.

### Evidence

- [md06_result.json](/home/_404/src/repo_intel/metadata_baseline/review/bundles/metadata-baseline-md06-006/md06_result.json)
- [outputs/asset-drift.app-server-protocol.json](/home/_404/src/repo_intel/metadata_baseline/review/bundles/metadata-baseline-md06-006/outputs/asset-drift.app-server-protocol.json)
- [outputs/asset-drift.plugins.json](/home/_404/src/repo_intel/metadata_baseline/review/bundles/metadata-baseline-md06-006/outputs/asset-drift.plugins.json)
- [outputs/asset-drift.exec-server.json](/home/_404/src/repo_intel/metadata_baseline/review/bundles/metadata-baseline-md06-006/outputs/asset-drift.exec-server.json)
- [outputs/asset-drift.crate-splits.json](/home/_404/src/repo_intel/metadata_baseline/review/bundles/metadata-baseline-md06-006/outputs/asset-drift.crate-splits.json)
- [evidence/just_test_md06.json](/home/_404/src/repo_intel/metadata_baseline/review/bundles/metadata-baseline-md06-006/evidence/just_test_md06.json)
- [evidence/just_ci.json](/home/_404/src/repo_intel/metadata_baseline/review/bundles/metadata-baseline-md06-006/evidence/just_ci.json)

### Observed shape

- app-server-protocol deleted in head: `12`
- plugin lifecycle signal count: `4`
- exec-server deleted in head: `3`
- `codex-login` present: `true`
- `codex-features` present: `false`

### Closeout

- scoped objective met
- protocol, plugin, execution, and crate-split drift preserved as first-class reports
- local snapshot truth remains explicit where upstream and local state diverge
- next patch set should start `MD-07`
