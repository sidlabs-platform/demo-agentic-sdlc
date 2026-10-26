# Epic: Admin Reporting and Export

| Field | Value |
|---|---|
| **Epic ID** | EPIC-006 |
| **Status** | Ready |
| **Owner** | Product / Engineering |
| **Created** | 2026-10-26 |
| **Target** | MVP |

## Goal / Objective
Give Admins aggregated course enrollment/completion statistics, learner-level progress for a course, and CSV export.

## Business Value
Provides visibility into course engagement and completion, supporting decisions about course improvement and learner support.

## BRD Requirements Mapped
| BRD ID | Description |
|---|---|
| BRD-FR-025–027 | Admin dashboard, per-course learner progress, CSV export |
| BRD-NFR-001, BRD-NFR-003, BRD-NFR-016–017 | Performance, Admin-only access, typed/tested APIs |

## Features
| Feature ID | Name | Priority | Status |
|---|---|---|---|
| FEAT-017 | Course and learner aggregates | P1 | Planned |
| FEAT-018 | CSV report export | P2 | Planned |

## Acceptance Criteria
1. Admin dashboard reports enrollment counts and completion rates per course.
2. Admin course learner report contains the progress fields defined in the Reporting LLD.
3. CSV export is streamed/downloadable; non-Admins are rejected.

## Dependencies & Risks
**Dependencies:** EPIC-001 schema, EPIC-002 RBAC, EPIC-005 progress data; HLD COMP-005.
**Risks:** Aggregate queries and export must handle empty datasets without errors.

## Out of Scope
- Advanced analytics, recommendations, and reporting beyond BRD-FR-025–027.

## Definition of Done
- [ ] All stories in this epic are Done
- [ ] Acceptance criteria verified
- [ ] Admin API endpoints documented
- [ ] No critical or high-severity bugs open
- [ ] Demo-ready for stakeholder review
