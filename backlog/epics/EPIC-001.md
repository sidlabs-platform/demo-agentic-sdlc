# Epic: Platform Foundation and Data

| Field | Value |
|---|---|
| **Epic ID** | EPIC-001 |
| **Status** | Ready |
| **Owner** | Product / Engineering |
| **Created** | 2026-10-26 |
| **Target** | MVP |

## Goal / Objective
Deliver the shared FastAPI configuration, SQLite persistence, application lifecycle, and starter-course data required by all platform capabilities.

## Business Value
Provides a reliable, secure, repeatable foundation so learner and admin workflows persist data and can be initialized consistently.

## BRD Requirements Mapped
| BRD ID | Description |
|---|---|
| BRD-FR-023 | Persist learner progress |
| BRD-FR-031–034 | Seed three structured starter courses and quizzes |
| BRD-NFR-001, BRD-NFR-004, BRD-NFR-006 | Performance, environment-based secrets, scoped CORS |
| BRD-NFR-009, BRD-NFR-011 | Durable data and published-course availability |
| BRD-NFR-015–017 | Typed, schema-based, tested implementation |

## Features
| Feature ID | Name | Priority | Status |
|---|---|---|---|
| FEAT-001 | Application settings and startup | P0 | Planned |
| FEAT-002 | SQLite schema and connection lifecycle | P0 | Planned |
| FEAT-003 | Starter course seed data | P0 | Planned |
| FEAT-004 | Final router wiring | P0 | Planned |

## Acceptance Criteria
1. The FastAPI application reads settings from environment variables and applies the configured CORS policy.
2. SQLite initializes all LLD entities with foreign-key enforcement and idempotent seed data for the three starter courses.
3. The application starts with persistence initialized and exposes all delivered API and HTML routers.

## Dependencies & Risks
**Dependencies:**
- BRD, HLD COMP-007, `docs/design/LLD/database.md`, and platform settings from COMP-001/003.

**Risks:**
- Schema/table omissions block several services; keep the schema aligned with all LLD entities and test initialization on a fresh database.

## Out of Scope
- Business logic for service-specific APIs.
- Production database migration or deployment infrastructure.

## Definition of Done
- [ ] All stories in this epic are Done
- [ ] Acceptance criteria verified
- [ ] Database setup is repeatable and tested
- [ ] No critical or high-severity bugs open
- [ ] Demo-ready for stakeholder review
