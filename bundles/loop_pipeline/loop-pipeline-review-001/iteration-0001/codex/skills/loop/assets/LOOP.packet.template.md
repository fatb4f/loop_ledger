# LOOP

## init
- wt: `$wt`
- repo_root: `<repo_root>`
- contract_root: `<contract_root>`

## loop_context
- objective: `<objective>`
- state_machine: `INIT -> PLAN -> DECISION -> IMPLEMENT -> VERIFY -> TERMINATE`

## phase_state
- current_phase: `INIT`
- next_phase: `PLAN`

## handoff
- request_instance: `$wt/PLAN/request.instance.json`
- request_validation: `$wt/PLAN/request.validation.json`
- batch_manifest: `$wt/PLAN/batch.manifest.json`
- response_manifest: `$wt/IMPLEMENT/response.manifest.json`

## transition_gate
- plan_to_implement: `PENDING`
- implement_to_verify: `PENDING`
- verify_to_terminate: `PENDING`

## verification
- live_contract_validation: `PENDING`
- request_response_linkage_valid: `PENDING`

## terminate
- reports_archive_ref: `<fill>`
- closeout_summary: `<fill>`

## rollback_path
- revert_mode: `retain_worktree`
- trigger: `verification_failed`
