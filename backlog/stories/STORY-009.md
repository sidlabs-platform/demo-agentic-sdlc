# Story: Track Completion and Show Learner Progress

| Field | Value |
|---|---|
| **Story ID** | STORY-009 |
| **Epic** | EPIC-005 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | L |
| **Priority** | P0 |

## User Story
**As a** Learner, **I want** lesson completion to update module/course progress and appear on my dashboard, **so that** I can resume learning without losing progress.

## Acceptance Criteria
1. **Given** an enrolled Learner completes a lesson, **When** the endpoint succeeds, **Then** the record is durably upserted before the response.
2. **Given** all module lessons or course modules are complete, **When** progress updates run, **Then** module completion and enrollment state transition transactionally.
3. **Given** the Learner refreshes the dashboard, **When** enrollment data is read, **Then** their current course and lesson/module counts are returned.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-020–024 | COMP-004, `LLD/progress-tracking.md` |
| BRD-NFR-001, BRD-NFR-009 | COMP-004/007 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-020 | Implement transactional lesson/module/course progress update | 8h |
| TASK-021 | Implement Learner dashboard data endpoint | 6h |

## UI/UX Notes
Progress dashboard and completion controls are covered by STORY-015 and STORY-014.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, aiosqlite transactions.
- **Key considerations:** State transitions `not_started → in_progress → completed`; progress persists before response.
- **Configuration:** Shared database settings.

## Dependencies
- TASK-020 consumes TASK-002, TASK-007, TASK-010, and enrollment service TASK-018. TASK-021 consumes TASK-018 and TASK-020.

## Definition of Done
- [ ] Transaction rollback, idempotent completion, state transitions, and learner scoping are tested
- [ ] No regressions in existing tests
