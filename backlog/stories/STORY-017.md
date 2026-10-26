# Story: View Admin Reports

| Field | Value |
|---|---|
| **Story ID** | STORY-017 |
| **Epic** | EPIC-007 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P1 |

## User Story
**As an** Admin, **I want** reporting dashboards and CSV export in the web UI, **so that** I can review outcomes and download data.

## Acceptance Criteria
1. **Given** report data, **When** `/admin/reports` loads, **Then** course enrollment/completion statistics and learner progress are presented.
2. **Given** an Admin selects CSV export, **When** the export endpoint responds, **Then** a downloadable file is offered.
3. **Given** an API error or empty report, **When** the UI renders, **Then** it shows an understandable empty/error state.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-042, BRD-FR-025–027 | COMP-006/005 |
| BRD-NFR-008 | COMP-006 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-030 | Build Admin reports dashboard UI | 6h |

## UI/UX Notes
Use stats cards and a course table, with a direct CSV download action.

## Technical Notes
- **Stack:** Jinja2, CSS, vanilla JS.
- **Key considerations:** Report APIs are Admin-only; escape report text and present numeric rates accurately.
- **Configuration:** None.

## Dependencies
- Reporting APIs TASK-023 and page route integration TASK-031.

## Definition of Done
- [ ] Report dashboard, export action, empty state, and responsive layout are verified
- [ ] No regressions in existing tests
