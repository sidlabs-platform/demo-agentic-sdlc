# Task: Implement Registration and Login APIs

| Field | Value |
|---|---|
| **Task ID** | TASK-006 |
| **Story** | STORY-002 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Wave**     | 2                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement the Auth service and `/api/v1/auth/register` and `/api/v1/auth/login` routes, including duplicate-email handling and required auth event logs.

## Implementation Details
**Files to create/modify:** `src/auth/service.py`, `src/auth/router.py`, `tests/auth/test_auth_api.py`.
**Approach:** Use aiosqlite and models/utilities from TASK-005. Registration inserts hashed password and returns UserResponse; login verifies credentials, returns bearer token; map duplicate email to 409 and invalid credentials to 401.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/auth/register` | POST | Create learner/admin account. |
| `/api/v1/auth/login` | POST | Authenticate and return JWT. |

Request/response: `RegisterRequest → UserResponse`; `LoginRequest → TokenResponse` per Auth LLD.

## Data Model Changes
Uses `users` from TASK-002; no schema changes.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | User persistence. |
| TASK-005 | Schemas, hashing, and token helpers. |

**Wave:** 2

## Acceptance Criteria
- [ ] Register/login status codes and responses match Auth LLD.
- [ ] Plaintext passwords are never persisted or returned; duplicate emails return 409.
- [ ] Successful and failed login events are logged without credentials.

## Test Requirements
- **Unit tests:** Service insert/authenticate behavior.
- **Integration tests:** Valid registration/login and duplicate/invalid credentials.
- **Edge cases:** Unknown email, malformed body, DB uniqueness race.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-002 |
| Epic | EPIC-002 |
| BRD | BRD-FR-001, BRD-FR-003, BRD-NFR-012, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Auth LLD COMP-001 sections 2, 4–6; use FastAPI dependency injection and Pydantic v2. Mounting routers occurs in TASK-031.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
