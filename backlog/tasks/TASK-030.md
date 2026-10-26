# Task: Build Admin Reports Dashboard UI

| Field | Value |
|---|---|
| **Task ID** | TASK-030 |
| **Story** | STORY-017 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 6h |
| **Type / Agent** | Frontend — `@5-ui-develop-agent` |

## Description
Build an Admin reporting page with aggregate stats, per-course learner details, and CSV download.

## Implementation Details
**Files to create/modify:**
- `src/templates/admin/reports.html`
- `src/static/css/admin-reports.css`, `src/static/js/admin-reports.js`
**Approach:** Follow COMP-006 reporting page design; use session/API helpers from TASK-024, call Admin reporting APIs, render returned counts/rates, show empty/error states, and expose CSV download.

## API Changes
Consumes dashboard report, per-course learners, and CSV export endpoints.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-024 | Shared page shell and session/API helpers. |
| TASK-023 | Reporting API contracts. |

**Wave:** 4

## Acceptance Criteria
- [ ] Course stats and selected course learner progress are visible.
- [ ] CSV action downloads the endpoint response.
- [ ] Empty and error responses are handled accessibly and without fabricated metrics.

## Test Requirements
- **Unit tests:** N/A — UI.
- **Integration tests:** Verify report rendering, course selection, and CSV action with mocked APIs.
- **Edge cases:** Empty report, invalid course, expired Admin token, export failure.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-017 |
| Epic | EPIC-007 |
| BRD | BRD-FR-042, BRD-FR-025–027, BRD-NFR-008 |

## Developer Agent Notes
`@5-ui-develop-agent`: Frontend LLD COMP-006 sections 2.2, 3.3, and 4.1; Reporting LLD COMP-005 section 4. Display server values as provided and do not add charting dependencies unless already approved.

## Definition of Done
- [ ] Reports, empty/error states, and export behavior verified
- [ ] Responsive desktop/tablet layout verified
- [ ] Acceptance criteria verified
