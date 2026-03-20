---
name: loop
description: "Use this meta-skill to orchestrate lifecycle routing across plan and implement with explicit transitions, live contract validation, and rollback-aware handoffs."
compatibility: "Requires child skills: plan and implement. No execution before decision APPROVED."
allowed-tools: "Read Bash(gh:*) Bash(git:*) Bash(scripts/validate_loop_packet.py:*) Bash(scripts/validate_handoff.py:*) Bash(scripts/validate_contract_bridge.py:*)"
metadata:
  author: _404
  version: "1.0"
---

# Loop

Meta-skill for routing and controlling bounded-batch lifecycle loops.

## Child skill routing

- `PLAN` phase -> use `plan` skill.
- `IMPLEMENT` phase -> use `implement` skill.
- `VERIFY` phase -> use `scripts/validate_contract_bridge.py`.

## State machine

`INIT -> PLAN -> DECISION -> IMPLEMENT -> VERIFY -> TERMINATE`
