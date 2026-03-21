# LOOP

## init
- wt: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0001`
- wt_role: `integration_worktree`
- ledger_wt: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0001`
- ledger_wt_role: `loop_ledger_worktree`
- repo_root: `/home/_404/src/runtime/asset-control-model`
- contract_root: `/home/_404/src/dotfiles/config/codex`

## loop_context
- objective: `Plan the tri-lane workbench integration across loop-pipeline, asset-control-model, and conversations_api`
- problem_set: `Current workbench planning spans multiple authority surfaces: workbench planning context, asset-control-model policy ownership, Codex loop/plan/implement controller contracts, loop_ledger review/evidence packaging, and the upcoming conversations_api request-response/session surface. The loop must normalize how these surfaces integrate before any broader tri-lane implementation plan is approved.`
- state_machine: `INIT -> PLAN -> DECISION -> IMPLEMENT -> VERIFY -> TERMINATE`

## phase_state
- current_phase: `IMPLEMENT`
- previous_phase: `DECISION`
- next_phase: `IMPLEMENT_REVIEW_OR_RESUME`

## handoff
- request_instance: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0001/PLAN/request.instance.json`
- request_validation: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0001/PLAN/request.validation.json`
- batch_manifest: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0001/PLAN/batch.manifest.json`
- response_manifest: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0001/IMPLEMENT/response.manifest.json`

## transition_gate
- plan_to_implement: `PENDING`
- implement_to_verify: `PENDING`
- verify_to_terminate: `PENDING`

## verification
- live_contract_validation: `PENDING`
- request_response_linkage_valid: `PENDING`
- pause_status: `paused_by_user`
- resume_prerequisites:
  - `Review the current Conversations API specification`
  - `Review other relevant OpenAI product and surface definitions`
  - `Model the review-request specification to use against that API surface`

## terminate
- reports_archive_ref: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0001/dist/workbench-tri-lane-001.iteration-0001.review.zip`
- ledger_bundle_ref: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0001/bundles/workbench/workbench-tri-lane-001/iteration-0001`
- closeout_summary: `Loop paused during IMPLEMENT pending Conversations API and adjacent OpenAI surface review before resuming the bounded slice.`

## rollback_path
- revert_mode: `retain_worktree`
- trigger: `verification_failed`
