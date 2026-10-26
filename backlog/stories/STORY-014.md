# Story: View Learner Progress Dashboard

| Field | Value |
|---|---|
| **Story ID** | STORY-014 |
| **Epic** | EPIC-007 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P0 |

## User Story
**As a** Learner, **I want** a dashboard of my enrolled courses and completion, **so that** I can resume learning efficiently.

## Acceptance Criteria
1. **Given** a signed-in Learner, **When** `/dashboard` loads, **Then** enrolled course cards show progress and resume links.
2. **Given** progress is persisted, **When** the page is refreshed, **Then** the same current progress is displayed.
3. **Given** a Learner follows the next lesson from the dashboard, **When** they navigate, **Then** the lesson is reachable within two clicks.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-036 | COMP-006 Frontend LLD; COMP-004 Progress LLD |
| BRD-NFR-007–008 | COMP-006 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-027 | Build learner dashboard/progress page | 6h |

## UI/UX Notes
Use the progress-bar partial and visible resume links; handle empty enrollment state.

## Technical Notes
- **Stack:** Jinja2, responsive CSS, vanilla JS.
- **Key considerations:** Display only data from authenticated learner endpoint.
- **Configuration:** None.

## Dependencies
- Learner dashboard API TASK-021 and page route integration TASK-031.

## Definition of Done
- [ ] Empty, partial, and completed progress states are verified
- [ ] Two-click navigation and responsive layout are verified
