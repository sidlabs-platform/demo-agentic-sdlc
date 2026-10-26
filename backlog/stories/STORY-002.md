# Story: Register and Sign In

| Field | Value |
|---|---|
| **Story ID** | STORY-002 |
| **Epic** | EPIC-002 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P0 |

## User Story
**As a** Learner or Admin, **I want** to register and sign in with email and password, **so that** I can securely use the platform.

## Acceptance Criteria
1. **Given** valid registration data, **When** submitted, **Then** a user is created with a password hash and no password is returned.
2. **Given** an existing email, **When** registration is submitted, **Then** the API returns 409.
3. **Given** valid credentials, **When** login is submitted, **Then** a signed expiring bearer token is returned; invalid credentials return 401.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-001, BRD-FR-003 | COMP-001, `LLD/auth.md` |
| BRD-NFR-004, BRD-NFR-012, BRD-NFR-015–017 | COMP-001 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-005 | Define auth schemas and password/JWT utilities | 6h |
| TASK-006 | Implement registration and login service/routes | 8h |

## UI/UX Notes
Public login and registration forms are delivered in STORY-012.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, bcrypt, JWT, aiosqlite.
- **Key considerations:** Never persist plaintext passwords or log credentials; match Auth LLD response/status contracts.
- **Configuration:** `SECRET_KEY`, `ACCESS_TOKEN_EXPIRE_MINUTES`.

## Dependencies
- Requires TASK-001 settings and TASK-002 user table before service/routes.

## Definition of Done
- [ ] Registration/login happy paths and failure cases are tested
- [ ] API schemas and auth events follow project conventions
- [ ] No regressions in existing tests
