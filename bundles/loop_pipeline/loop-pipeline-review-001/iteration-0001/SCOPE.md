# Loop Pipeline Review Scope

This bundle captures the current loop pipeline authority across two surfaces:

- `$CODEX_HOME` workflow/control assets that define loop, plan, implement, and git-flow behavior
- `loop_ledger` controller assets that define review manifests, evidence gating, lineage, and shareable review outputs

Included categories:

- Codex control: `control/git-flow/*`, `plan.request_response_contract.v1.json`, workflow prompt reference, consolidated bundle note
- Codex skills: `skills/loop/*`, `skills/plan/*`, `skills/implement/*`, `skills/registry.json`
- Ledger controller: `AGENTS.md`, `README.md`, `justfile`, `schemas/*`, `scripts/*`
- Ledger manifests: `manifests/metadata_baseline/*.json`
- Ledger review outputs: `dist/*.review.zip`

Heads:

- dotfiles/codex surface: `577fc239ae2673df9d5769ed8aa5d80430d80de3`
- loop_ledger: `5196465ced560a5ea263db5b6721cb2b369fb1a8`
