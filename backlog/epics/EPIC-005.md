# Epic: Learner Enrollment and Progress

| Field | Value |
|---|---|
| **Epic ID** | EPIC-005 |
| **Status** | Ready |
| **Owner** | Product / Engineering |
| **Created** | 2026-10-26 |
| **Target** | MVP |

## Goal / Objective
Let Learners enroll in published courses, record lesson completion durably, and retrieve their own course progress.

## Business Value
Makes course participation measurable and lets Learners resume where they left off, including after a page refresh.

## BRD Requirements Mapped
| BRD ID | Description |
|---|---|
| BRD-FR-019–024 | Enrollment, lesson/module/course completion, persistence, learner dashboard API |
| BRD-NFR-001, BRD-NFR-009 | API performance and durable progress |

## Features
| Feature ID | Name | Priority | Status |
|---|---|---|---|
| FEAT-014 | Published-course enrollment | P0 | Planned |
| FEAT-015 | Transactional progress updates | P0 | Planned |
| FEAT-016 | Learner dashboard data | P0 | Planned |

## Acceptance Criteria
1. A Learner can enroll once in a published course; duplicate or unpublished enrollment is rejected.
2. Completing a lesson persists progress before response and automatically updates module/course status transactionally.
3. The dashboard returns only the authenticated Learner's enrollments and progress counts.

## Dependencies & Risks
**Dependencies:** EPIC-001 database, EPIC-002 identity, EPIC-003 course and lesson data; HLD COMP-004.
**Risks:** Partial progress updates must not survive a failed transaction.

## Out of Scope
- Admin reporting and manual Admin enrollment/removal (not specified by the detailed service design).

## Definition of Done
- [ ] All stories in this epic are Done
- [ ] Acceptance criteria verified
- [ ] Endpoints and service flows tested
- [ ] No critical or high-severity bugs open
- [ ] Demo-ready for stakeholder review
