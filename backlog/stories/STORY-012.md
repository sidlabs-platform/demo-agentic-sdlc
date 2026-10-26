# Story: Browse Courses and Course Details

| Field | Value |
|---|---|
| **Story ID** | STORY-012 |
| **Epic** | EPIC-007 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P0 |

## User Story
**As a** Learner, **I want** to browse published courses and inspect their modules/lessons, **so that** I can choose what to learn.

## Acceptance Criteria
1. **Given** published courses, **When** `/courses` loads, **Then** responsive course cards show title, description, difficulty, and enrollment action.
2. **Given** a selected course, **When** its detail page loads, **Then** ordered modules and lesson links are shown.
3. **Given** enrollment is requested from the catalog, **When** the API responds, **Then** success or API errors are presented without losing page context.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-037–038 | COMP-006 Frontend LLD; COMP-002 Course LLD |
| BRD-NFR-008 | COMP-006 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-025 | Build catalog and course detail templates/interactions | 7h |

## UI/UX Notes
Reuse course-card partial; maintain obvious enrollment and lesson navigation.

## Technical Notes
- **Stack:** Jinja2, responsive CSS, vanilla JS `fetch()`.
- **Key considerations:** Use course API; show only server-returned published courses for Learners.
- **Configuration:** None.

## Dependencies
- Course API TASK-009 and enrollment API TASK-019; page route integration TASK-031.

## Definition of Done
- [ ] Catalog/detail display and enrollment errors are verified
- [ ] No regressions in existing tests
