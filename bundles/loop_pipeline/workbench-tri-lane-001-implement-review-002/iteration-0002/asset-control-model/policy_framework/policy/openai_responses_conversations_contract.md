# OpenAI Responses + Conversations Contract

This contract freezes the minimum OpenAI-backed runtime authority needed for
the paused tri-lane workbench loop.

## Runtime authority

- Primary runtime surface: `Responses API`
- Durable state surface: `Conversation state`
- Async lifecycle surfaces: `Background mode`, `Webhooks`
- Realtime extension surface: `Realtime API`

## ACM-owned contract objects

- `openai_conversation_context.v1`
- `openai_response_request.v1`
- `openai_response_snapshot.v1`
- `openai_review_request.v1`
- `openai_review_verdict.v1`
- `openai_responses_conversations_contract_manifest.v1`

## Review pattern

The contract assumes a dual-thread review loop:

- work conversation: plan + implementation history
- reviewer conversation: durable judge policy + few-shot review examples

Reviewer output must be constrained with Structured Outputs and validated against
`openai_review_verdict.schema.json`.

## Scope guard

This freeze does not implement:

- transport/client/server runtime behavior
- collector code for API events
- webhook receivers
- realtime session management

It only freezes the boundary objects and authority refs needed to rebase the
paused loop onto the actual OpenAI API surface.
