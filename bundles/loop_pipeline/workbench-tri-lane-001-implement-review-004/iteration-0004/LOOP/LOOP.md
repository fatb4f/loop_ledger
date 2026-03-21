# LOOP

## init
- wt: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0004`
- wt_role: `integration_worktree`
- ledger_wt: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0004`
- ledger_wt_role: `loop_ledger_worktree`
- repo_root: `/home/_404/src/runtime/asset-control-model`
- contract_root: `/home/_404/src/dotfiles/config/codex`

## loop_context
- objective: `Plan the tri-lane workbench integration across loop-pipeline, asset-control-model, and conversations_api`
- problem_set: `Current workbench planning spans multiple authority surfaces: workbench planning context, asset-control-model policy ownership, Codex loop/plan/implement controller contracts, loop_ledger review/evidence packaging, and the upcoming conversations_api request-response/session surface. The loop must normalize how these surfaces integrate before any broader tri-lane implementation plan is approved.`
- state_machine: `INIT -> PLAN -> DECISION -> IMPLEMENT -> VERIFY -> TERMINATE`

## phase_state
- current_phase: `IMPLEMENT`
- previous_phase: `IMPLEMENT`
- next_phase: `IMPLEMENT_REVIEW_OR_RESUME`

## handoff
- request_instance: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0004/PLAN/request.instance.json`
- request_validation: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0004/PLAN/request.validation.json`
- batch_manifest: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0004/PLAN/batch.manifest.json`
- response_manifest: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0004/IMPLEMENT/response.manifest.json`
- prior_review_reply: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0004/REVIEW/review.reply.previous.iteration-0003.json`
- current_review_request: `/home/_404/src/_worktrees/workbench-tri-lane-001.iteration-0004/REVIEW/review.request.json`

## transition_gate
- plan_to_implement: `PENDING`
- implement_to_verify: `PENDING`
- verify_to_terminate: `PENDING`

## verification
- live_contract_validation: `PENDING`
- request_response_linkage_valid: `PENDING`
- pause_status: `iteration_rework_scaffold_open`
- resume_prerequisites:
  - `Validate the rebased inventory and bundle-boundary artifacts in iteration-0004`
  - `Materialize the implement review request bundle under iteration-0004`
  - `Hold implement_to_verify and promotion pending until the rebased slice is reviewed`

## terminate
- reports_archive_ref: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0004/dist/workbench-tri-lane-001-implement-review-004.iteration-0004.review.zip`
- ledger_bundle_ref: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0004/bundles/loop_pipeline/workbench-tri-lane-001-implement-review-004/iteration-0004`
- closeout_summary: `Iteration-0004 carries forward the captured iteration-0003 review reply and completes the actual official-surface OpenAI-backed lane rebase. The rebased slice now waits on implement review before any VERIFY transition.`

## rollback_path
- revert_mode: `retain_worktree`
- trigger: `verification_failed`
