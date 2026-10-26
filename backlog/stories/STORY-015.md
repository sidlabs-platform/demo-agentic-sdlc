# Story: Manage Courses from the Admin UI

| Field | Value |
|---|---|
| **Story ID** | STORY-015 |
| **Epic** | EPIC-007 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | L |
| **Priority** | P0 |

## User Story
**As an** Admin, **I want** course, module, lesson, and quiz management pages, **so that** I can author and publish learning content.

## Acceptance Criteria
1. **Given** Admin access, **When** `/admin/courses` loads, **Then** courses show draft/published status and create/edit/delete/publish actions.
2. **Given** course structure is edited, **When** module/lesson/quiz operations run, **Then** their APIs are used and errors are shown.
3. **Given** a course is not ready, **When** publish fails, **Then** the UI explains the API validation response and does not imply publication.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-040 | COMP-006 Frontend LLD |
| BRD-FR-004–018 | COMP-002 Course Management LLD |
| BRD-NFR-008 | COMP-006 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-028 | Build Admin course/content management UI | 9h |

## UI/UX Notes
Use a manageable course table and clear editing forms; avoid new frontend frameworks.

## Technical Notes
- **Stack:** Jinja2, CSS, vanilla JS.
- **Key considerations:** Admin APIs enforce authorization; UI must not claim success until the API confirms.
- **Configuration:** None.

## Dependencies
- Course routes TASK-009, module/lesson routes TASK-011, sanitized retrieval TASK-013, quiz endpoints TASK-014, and TASK-031.

## Definition of Done
- [ ] Course lifecycle and child content workflows are verified
- [ ] Responsive Admin layout and API error states are verified
