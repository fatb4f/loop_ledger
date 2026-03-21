# OpenAI Surface Review

## Purpose

Freeze the OpenAI-backed authority surfaces that must replace the current provisional `conversations_api` lane model before the paused tri-lane loop resumes.

## 1. Current Conversations API definition

Primary authority:
- `Responses API`
- `Conversation state`

Current documented shape:
- OpenAI recommends the `Responses API` for multi-turn stateful interaction.
- The `Conversations API` works with the `Responses API` to persist conversation state as a durable object with its own identifier.
- Conversations store `items`, including messages, tool calls, and tool outputs.
- A lighter-weight continuation path also exists through `previous_response_id`.

Implication for the loop:
- the lane should not model only `conversation_request.json` and `conversation_response.json`
- it must model durable conversation identity plus response/item lineage
- `previous_response_id` needs to be treated as a first-class linkage edge when a durable conversation object is not used

## 2. Other relevant OpenAI surfaces

Required adjacent surfaces:
- `Background mode`
- `Webhooks`
- `Realtime API`

Why they matter:
- `Background mode` adds asynchronous response lifecycle and terminal status handling
- `Webhooks` add server-side event delivery for background responses and other long-running jobs
- `Realtime API` adds a distinct conversation-management surface over persistent connections

Secondary surfaces to track:
- `ChatKit`
- `Apps SDK`
- `ChatGPT Actions`

Why they matter:
- they are not the primary runtime authority for this lane
- they do affect packaging, UI/state ownership, and future integration boundaries

## 3. Review-request model to use

The loop should review against a `review_request` shape rooted in official OpenAI response and conversation semantics, not the earlier placeholder names.

Recommended review-request objects:
- `conversation_context`
  - `mode`: `conversation` or `previous_response_chain`
  - `conversation_id`
  - `previous_response_id`
- `request`
  - `request_id`
  - `model`
  - `input`
  - `instructions`
  - `tools`
  - `background`
  - `stream`
  - `store`
- `response`
  - `response_id`
  - `status`
  - `output_items`
  - `output_text`
- `events`
  - streaming events when `stream=true`
  - webhook events when `background=true`
- `provenance`
  - source root
  - controller root
  - policy root
  - ledger root
  - official OpenAI surface refs used by the request

## Recommended lane decision

Use this as the lane baseline:
- primary runtime surface: `Responses API`
- durable state surface: `Conversations API`
- async lifecycle surface: `Background mode` + `Webhooks`
- realtime extension surface: `Realtime API`

Do not resume the current bounded slice until the inventory and bundle-boundary artifacts are rebased on that model.

## Sources

- `Conversation state`: https://developers.openai.com/api/docs/guides/conversation-state
- `Background mode`: https://developers.openai.com/api/docs/guides/background
- `Webhooks`: https://developers.openai.com/api/docs/guides/webhooks
- `Migrate to the Responses API`: https://developers.openai.com/api/docs/guides/migrate-to-responses
- `Realtime API`: https://developers.openai.com/api/docs/guides/realtime

