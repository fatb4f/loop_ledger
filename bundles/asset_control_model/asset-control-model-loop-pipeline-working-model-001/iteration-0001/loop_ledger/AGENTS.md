# AGENTS.md

## Role

This repo is a controller and evidence ledger for looped work. It is not the implementation repo.

## Rules

1. Use the root [justfile](/home/_404/src/loop_ledger/justfile) as the primary control surface.
2. Prefer editing schemas, manifests, and bundle scripts here instead of manually copying review files.
3. Do not treat files in this repo as implementation authority for upstream projects.
4. Upstream source repos remain authoritative for code, tests, and runtime artifacts.
5. A materialized bundle in this repo is copied review evidence, not the source of truth.
6. When adding a new project bundle:
   - add a manifest under `manifests/<project>/`
   - validate it against `schemas/`
   - materialize it into `bundles/<project>/...`
   - declare required outputs and required check evidence in `evidence_bundle`
   - when a bundle is derived from a parent plan bundle, declare `lineage`
    - expect bundle generation to fail if that evidence is missing
7. Keep bundles small and review-facing:
   - copy packet summaries and review artifacts
   - keep deep provenance as refs when possible
   - do not copy whole implementation trees

## Layout

- `schemas/`: JSON schemas for review manifests and bundle metadata
- `scripts/`: narrow validation and materialization scripts
- `manifests/`: project-specific review-bundle manifests
- `bundles/`: generated review bundles

## Current controller targets

- validate a review manifest
- materialize a review bundle
- seed the metadata_baseline parent planning bundle
- seed the metadata_baseline md01 bundle
