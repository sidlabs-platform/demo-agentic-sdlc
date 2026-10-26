# Story: View and Export Admin Reports

| Field | Value |
|---|---|
| **Story ID** | STORY-010 |
| **Epic** | EPIC-006 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | L |
| **Priority** | P1 |

## User Story
**As an** Admin, **I want** course statistics, learner progress, and CSV exports, **so that** I can monitor outcomes and analyze participation.

## Acceptance Criteria
1. **Given** course enrollment records, **When** an Admin requests dashboard statistics, **Then** per-course enrollment/completion data and totals are returned.
2. **Given** a course ID, **When** an Admin requests its learner report, **Then** progress details are returned or 404 for an unknown course.
3. **Given** an Admin requests CSV export, **When** records exist or are empty, **Then** a valid downloadable CSV response is streamed.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-025–027 | COMP-005, `LLD/reporting.md` |
| BRD-NFR-001, BRD-NFR-003, BRD-NFR-016–017 | COMP-001/005 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-022 | Implement report schemas and aggregate/export service | 8h |
| TASK-023 | Expose Admin reporting endpoints | 5h |

## UI/UX Notes
Admin report page is covered by STORY-018.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, aiosqlite, StreamingResponse.
- **Key considerations:** Read-only queries; Admin-only access; handle zero enrollments safely.
- **Configuration:** Shared database settings.

## Dependencies
- TASK-022 requires TASK-002 schema; TASK-023 requires TASK-007 RBAC and TASK-022 service.

## Definition of Done
- [ ] Aggregate math, 404, authorization, empty exports, and CSV escaping are tested
- [ ] No regressions in existing tests
