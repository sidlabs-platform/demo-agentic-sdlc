# Task: Implement Current-User and Role Dependencies

| Field | Value |
|---|---|
| **Task ID** | TASK-007 |
| **Story** | STORY-003 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 5h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Provide reusable FastAPI dependencies that authenticate JWT bearer tokens, load the user identity, and enforce the Admin/Learner roles.

## Implementation Details
**Files to create/modify:** `src/auth/dependencies.py`, `tests/auth/test_dependencies.py`.
**Approach:** Implement `get_current_user()` and `require_role(role)` per Auth LLD. Derive identity from verified token, then load/validate the user; return 401 on absent/invalid identity and 403 for insufficient role.

## API Changes
N/A — shared route dependencies.

## Data Model Changes
Reads `users` table; no schema changes.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Load user records. |
| TASK-005 | Verify token and define role models. |

**Wave:** 2

## Acceptance Criteria
- [ ] Missing, malformed, expired, or invalid tokens return 401.
- [ ] Role mismatch returns 403; allowed roles pass and provide verified user.
- [ ] User identity is never accepted from an untrusted request field.

## Test Requirements
- **Unit tests:** Dependency behavior for both roles and token errors.
- **Integration tests:** Protected route test with admin, learner, and anonymous client.
- **Edge cases:** Valid token for deleted user and unknown role.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-003 |
| Epic | EPIC-002 |
| BRD | BRD-FR-002, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Auth LLD COMP-001 sections 2.2, 2.3, 4, and 6. Export `get_current_user` and `require_role` for all service routers.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
