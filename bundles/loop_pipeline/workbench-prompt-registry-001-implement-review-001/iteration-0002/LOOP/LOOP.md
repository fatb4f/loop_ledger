# LOOP

## init
- wt: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0002`
- wt_role: `integration_worktree`
- ledger_wt: `/home/_404/src/loop_ledger.worktrees/workbench-prompt-registry-001.iteration-0002`
- ledger_wt_role: `loop_ledger_worktree`
- repo_root: `/home/_404/src/runtime/asset-control-model`
- contract_root: `/home/_404/src/dotfiles/config/codex`

## loop_context
- objective: `Operationalize prompt-registry as a derived retrieval and assembly overlay over canonical control authority`
- problem_set: `prompt-registry is currently declarative metadata. This loop must define the first bounded contract/controller slice that makes it operational without allowing the overlay to become workflow authority.`
- state_machine: `INIT -> PLAN -> DECISION -> IMPLEMENT -> VERIFY -> TERMINATE`

## phase_state
- current_phase: `VERIFY`
- previous_phase: `IMPLEMENT`
- next_phase: `TERMINATE`

## handoff
- request_instance: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0002/PLAN/request.instance.json`
- request_validation: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0002/PLAN/request.validation.json`
- batch_manifest: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0002/PLAN/batch.manifest.json`
- response_manifest: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0002/IMPLEMENT/response.manifest.json`

## transition_gate
- plan_to_implement: `PASS`
- implement_to_verify: `PASS`
- verify_to_terminate: `PENDING`

## verification
- live_contract_validation: `PENDING`
- request_response_linkage_valid: `PENDING`
- pause_status: `verify_open_from_accepted_implement_review`
- resume_prerequisites:
  - `Run VERIFY-phase contract and linkage validation`
  - `Keep promotion pending until VERIFY passes`

## terminate
- reports_archive_ref: `/home/_404/src/loop_ledger/dist/workbench-prompt-registry-001-implement-review-001.iteration-0002.review.zip`
- ledger_bundle_ref: `/home/_404/src/loop_ledger/bundles/loop_pipeline/workbench-prompt-registry-001-implement-review-001/iteration-0002`
- closeout_summary: `Implement review accepted; VERIFY opened.`

## rollback_path
- revert_mode: `retain_worktree`
- trigger: `verification_failed`
