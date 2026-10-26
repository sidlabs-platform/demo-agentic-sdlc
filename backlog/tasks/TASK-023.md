# Task: Expose Admin Reporting Endpoints

| Field | Value |
|---|---|
| **Task ID** | TASK-023 |
| **Story** | STORY-010 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 5h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Expose Admin-only dashboard, course learner progress, and CSV export endpoints.

## Implementation Details
**Files to create/modify:** `src/reporting/router.py`, `tests/reporting/test_reporting_api.py`.
**Approach:** Use TASK-022 service and response models, `require_role("admin")`, return FastAPI StreamingResponse for CSV with appropriate content type/disposition, map missing course to 404.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/admin/reports/dashboard` | GET | Course aggregates. |
| `/api/v1/admin/reports/courses/{id}/learners` | GET | Learner-level course progress. |
| `/api/v1/admin/reports/export?format=csv` | GET | CSV download. |

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-007 | Admin role authorization. |
| TASK-022 | Typed report service and CSV source. |

**Wave:** 3

## Acceptance Criteria
- [ ] All routes require Admin and match Reporting LLD response/status contracts.
- [ ] CSV is downloadable with correct response headers.
- [ ] Unknown course returns 404; unsupported format is handled clearly.

## Test Requirements
- **Unit tests:** N/A — service in TASK-022.
- **Integration tests:** Each route, role enforcement, response headers.
- **Edge cases:** Empty export and unknown course.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-010 |
| Epic | EPIC-006 |
| BRD | BRD-FR-025–027, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Reporting LLD COMP-005 sections 4 and 5.2. Register router in TASK-031; protect every route with Admin role.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] API docs and route tests cover each endpoint
- [ ] Acceptance criteria verified
