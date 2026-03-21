# LOOP

## init
- wt: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0001`
- wt_role: `integration_worktree`
- ledger_wt: `/home/_404/src/loop_ledger.worktrees/workbench-prompt-registry-001.iteration-0001`
- ledger_wt_role: `loop_ledger_worktree`
- repo_root: `/home/_404/src/runtime/asset-control-model`
- contract_root: `/home/_404/src/dotfiles/config/codex`

## loop_context
- objective: `Operationalize prompt-registry as a derived retrieval and assembly overlay over canonical control authority`
- problem_set: `prompt-registry is currently declarative metadata. This loop must define the first bounded contract/controller slice that makes it operational without allowing the overlay to become workflow authority.`
- state_machine: `INIT -> PLAN -> DECISION -> IMPLEMENT -> VERIFY -> TERMINATE`

## phase_state
- current_phase: `IMPLEMENT`
- previous_phase: `DECISION`
- next_phase: `VERIFY`

## handoff
- request_instance: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0001/PLAN/request.instance.json`
- request_validation: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0001/PLAN/request.validation.json`
- batch_manifest: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0001/PLAN/batch.manifest.json`
- response_manifest: `/home/_404/src/_worktrees/workbench-prompt-registry-001.iteration-0001/IMPLEMENT/response.manifest.json`

## transition_gate
- plan_to_implement: `PASS`
- implement_to_verify: `PENDING`
- verify_to_terminate: `PENDING`

## verification
- live_contract_validation: `PENDING`
- request_response_linkage_valid: `PENDING`
- pause_status: `implement_open_from_approved_plan`
- resume_prerequisites:
  - `Emit the four bounded IMPLEMENT artifacts`
  - `Verify authority refs resolve under control`
  - `Submit the IMPLEMENT packet for review`

## terminate
- reports_archive_ref: `/home/_404/src/loop_ledger/dist/workbench-prompt-registry-001-plan-review-001.iteration-0001.review.zip`
- ledger_bundle_ref: `/home/_404/src/loop_ledger/bundles/loop_pipeline/workbench-prompt-registry-001-plan-review-001/iteration-0001`
- closeout_summary: `Pending`

## rollback_path
- revert_mode: `retain_worktree`
- trigger: `verification_failed`
