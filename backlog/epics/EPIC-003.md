# Epic: Course and Learning Content Management

| Field | Value |
|---|---|
| **Epic ID** | EPIC-003 |
| **Status** | Ready |
| **Owner** | Product / Engineering |
| **Created** | 2026-10-26 |
| **Target** | MVP |

## Goal / Objective
Enable Admins to author and manage courses, modules, lessons, and quizzes, and enable authorized users to retrieve safe course and lesson content.

## Business Value
Supplies the structured, governed learning material Learners need and the authoring workflows Admins need.

## BRD Requirements Mapped
| BRD ID | Description |
|---|---|
| BRD-FR-004–018 | Course/module/lesson/quiz CRUD, catalog/detail, sanitization, quiz scoring |
| BRD-NFR-001, BRD-NFR-003, BRD-NFR-005, BRD-NFR-011 | Performance, RBAC, XSS prevention, AI-independent published content |
| BRD-NFR-015–017 | Typed models, Pydantic schemas, endpoint/service tests |

## Features
| Feature ID | Name | Priority | Status |
|---|---|---|---|
| FEAT-007 | Course lifecycle and discovery API | P0 | Planned |
| FEAT-008 | Module and lesson authoring API | P0 | Planned |
| FEAT-009 | Sanitized lesson delivery | P0 | Planned |
| FEAT-010 | Quiz management and attempts | P0 | Planned |

## Acceptance Criteria
1. Admin course and content CRUD, publish/unpublish, and role-aware catalog/detail behavior match the BRD endpoints.
2. Learner-facing lesson HTML is sanitized and quiz attempts return scores and explanations without exposing correct answers in question responses.
3. Published courses remain readable from SQLite when the AI provider is unavailable.

## Dependencies & Risks
**Dependencies:** EPIC-001 database, EPIC-002 RBAC; HLD COMP-002 and corresponding Course Management LLD.
**Risks:** Keep learner-facing lesson rendering sanitized and validate publish rules before changing course status.

## Out of Scope
- AI provider calls, enrollment/progress state, and admin reports.

## Definition of Done
- [ ] All stories in this epic are Done
- [ ] Acceptance criteria verified
- [ ] API endpoints documented
- [ ] No critical or high-severity bugs open
- [ ] Demo-ready for stakeholder review
