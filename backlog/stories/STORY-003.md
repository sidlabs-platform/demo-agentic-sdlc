# Story: Enforce Role-Based Access

| Field | Value |
|---|---|
| **Story ID** | STORY-003 |
| **Epic** | EPIC-002 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | S |
| **Priority** | P0 |

## User Story
**As a** Learner or Admin, **I want** each protected action checked against my identity and role, **so that** restricted data and operations remain protected.

## Acceptance Criteria
1. **Given** no or invalid bearer token, **When** a protected route is called, **Then** the dependency returns 401.
2. **Given** a Learner calls an Admin-only route, **When** role authorization runs, **Then** the request returns 403.
3. **Given** a valid token, **When** a route requests the current user, **Then** the verified user ID and role are available to the handler.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-002 | COMP-001, `LLD/auth.md` |
| BRD-NFR-003, BRD-NFR-012 | COMP-001 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-007 | Implement token identity and role dependencies | 5h |

## UI/UX Notes
N/A — shared API dependency.

## Technical Notes
- **Stack:** FastAPI `Depends()`, JWT utility from Auth LLD.
- **Key considerations:** Use `get_current_user()` and `require_role()` as reusable dependencies; do not trust client-supplied user IDs.
- **Configuration:** Uses shared JWT settings.

## Dependencies
- TASK-002 user table and TASK-005 token helpers.

## Definition of Done
- [ ] Missing, invalid, expired, and insufficient-role cases are tested
- [ ] Services use authenticated identity rather than request-supplied identity
- [ ] No regressions in existing tests
