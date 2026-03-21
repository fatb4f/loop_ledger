package policy

// Initial package boundary for cross-document policy.
// This stays intentionally small on the contract branch: it declares the
// control-plane shape without pretending the full admissibility model exists yet.

control_plane: {
  authority: {
    cargo: "workspace/package truth and compiled execution"
    just: "operator-facing command surface"
    json_schema: "boundary validation for runtime JSON objects"
    cue: "primary admissibility engine for workflow state; cross-document invariants and derivation"
    jq: "read-only observation and assertions"
  }

  required_layers: [
    "schemas",
    "policy",
    "manifests",
    "events",
    "workspaces",
  ]
}
