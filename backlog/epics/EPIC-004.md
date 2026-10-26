# Epic: AI Content Generation and Governance

| Field | Value |
|---|---|
| **Epic ID** | EPIC-004 |
| **Status** | Ready |
| **Owner** | Product / Engineering |
| **Created** | 2026-10-26 |
| **Target** | MVP |

## Goal / Objective
Provide an Admin-only, pluggable GitHub Models integration that generates auditable draft lesson/quiz artifacts and supports explicit review, approval, and regeneration.

## Business Value
Accelerates course authoring while preserving human review and preventing unapproved AI content from becoming learner-visible.

## BRD Requirements Mapped
| BRD ID | Description |
|---|---|
| BRD-FR-028–030 | Draft artifacts, explicit approval, AI-generated label |
| BRD-INT-001–007 | GitHub Models, request/artifact storage, retries, safe errors, regeneration, pluggable interface |
| BRD-NFR-002, BRD-NFR-004, BRD-NFR-010, BRD-NFR-013–014 | Generation duration, secret handling, retryable errors, logging/latency |

## Features
| Feature ID | Name | Priority | Status |
|---|---|---|---|
| FEAT-011 | Pluggable GitHub Models client | P0 | Planned |
| FEAT-012 | Draft generation and artifact lifecycle | P0 | Planned |
| FEAT-013 | Admin approve and regenerate APIs | P0 | Planned |

## Acceptance Criteria
1. Generation calls use environment-configured GitHub Models settings and a swappable protocol implementation.
2. Requests and draft artifacts persist with request status and provenance; no generated content is auto-published.
3. 429/5xx failures use bounded exponential backoff, and safe retryable errors/logs never expose API keys.

## Dependencies & Risks
**Dependencies:** EPIC-001 persistence/configuration, EPIC-002 Admin authorization; HLD COMP-003 and AI Generation LLD.
**Risks:** Provider availability/rate limits and generated-content quality; retain explicit Admin review.

## Out of Scope
- Future MCP implementation, model training, and automatic publication.

## Definition of Done
- [ ] All stories in this epic are Done
- [ ] Acceptance criteria verified
- [ ] AI API documented and externally mocked in tests
- [ ] No critical or high-severity bugs open
- [ ] Demo-ready for stakeholder review
