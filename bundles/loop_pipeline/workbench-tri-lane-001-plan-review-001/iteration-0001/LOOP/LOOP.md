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
- current_phase: `PLAN`
- previous_phase: `INIT`
- next_phase: `DECISION`

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

## terminate
- reports_archive_ref: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0001/dist/workbench-tri-lane-001.iteration-0001.review.zip`
- ledger_bundle_ref: `/home/_404/src/loop_ledger.worktrees/workbench-tri-lane-001.iteration-0001/bundles/workbench/workbench-tri-lane-001/iteration-0001`
- closeout_summary: `Loop initialized; planning packet scaffold created; decision pending.`

## rollback_path
- revert_mode: `retain_worktree`
- trigger: `verification_failed`
