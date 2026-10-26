# Task: Define Auth Schemas and Security Utilities

| Field | Value |
|---|---|
| **Task ID** | TASK-005 |
| **Story** | STORY-002 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 6h |
| **Wave**     | 1                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Create the Pydantic request/response models and isolated password/JWT utilities required by registration, login, and RBAC.

## Implementation Details
**Files to create/modify:** `src/auth/__init__.py`, `src/auth/models.py`, `src/auth/utils.py`, `tests/auth/test_utils.py`.
**Approach:** Implement RegisterRequest, LoginRequest, TokenResponse, UserResponse; use bcrypt hashing and JWT encode/decode with app settings. UserResponse must omit password hashes. Include type hints and docstrings.

## API Changes
N/A — schemas/utilities only.

## Data Model Changes
N/A — users table is defined in TASK-002.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-001 | Requires secret/token settings. |

**Wave:** 1

## Acceptance Criteria
- [ ] Request validation follows Auth LLD constraints and response excludes password data.
- [ ] Password verify/hash and token create/verify helpers work with configured secret/expiry.
- [ ] Invalid/expired tokens fail closed.

## Test Requirements
- **Unit tests:** Schema validation, hash/verify, token claims and expiration.
- **Integration tests:** N/A — route behavior in TASK-006/007.
- **Edge cases:** Wrong password, malformed token, expired token, invalid roles.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-002 |
| Epic | EPIC-002 |
| BRD | BRD-FR-001, BRD-FR-003, BRD-NFR-004, BRD-NFR-015–017 |

## Developer Agent Notes
`@4-develop-agent`: Auth LLD COMP-001 sections 2–3, 6–7. Use the configured secret only; never log password, token, or secret values.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
