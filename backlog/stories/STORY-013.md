# Story: Study Lessons and Complete Them

| Field | Value |
|---|---|
| **Story ID** | STORY-013 |
| **Epic** | EPIC-007 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P0 |

## User Story
**As a** Learner, **I want** a lesson viewer with safe content and completion controls, **so that** I can study and record my progress.

## Acceptance Criteria
1. **Given** a lesson, **When** `/lessons/{id}` renders, **Then** its sanitized HTML is displayed with lesson navigation.
2. **Given** the Learner marks a lesson complete, **When** the completion API succeeds, **Then** the UI confirms the durable update and refreshes progress state.
3. **Given** content contains executable markup, **When** displayed, **Then** it cannot execute in the browser.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-018, BRD-FR-039 | COMP-006 Frontend LLD; COMP-002 Course LLD |
| BRD-NFR-005, BRD-NFR-007–008 | COMP-002/006 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-026 | Build lesson viewer and completion interaction | 6h |

## UI/UX Notes
Use the pre-sanitized lesson response; provide previous/next and mark-complete controls.

## Technical Notes
- **Stack:** Jinja2, HTML/CSS/JS.
- **Key considerations:** Never render raw Markdown or add unsafe HTML; use bearer-authenticated lesson and completion APIs.
- **Configuration:** None.

## Dependencies
- Sanitized lesson API TASK-013, lesson completion TASK-020, and page route integration TASK-031.

## Definition of Done
- [ ] Sanitized display, completion state, and API error feedback are verified
- [ ] Dashboard-to-next-lesson navigation stays within two clicks
