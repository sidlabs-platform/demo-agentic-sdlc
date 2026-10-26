# Task: Initialize Persistence During Application Lifespan

| Field | Value |
|---|---|
| **Task ID** | TASK-004 |
| **Story** | STORY-001 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 3h |
| **Wave**     | 3                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Connect database initialization, starter seeding, and shutdown cleanup to the FastAPI application lifespan.

## Implementation Details
**Files to create/modify:**
- `src/database/init.py` — initialization entry point if needed.
- `src/main.py` — lifespan invokes schema/init and seed functions from TASK-002/003.
- `tests/test_app_lifespan.py` — isolated lifecycle tests.

**Approach:** Use FastAPI lifespan; initialize once before serving requests and close resources on shutdown. Keep DB path configurable and do not make app import perform I/O.

## API Changes
N/A.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-001 | App/settings foundation. |
| TASK-002 | Database connection/schema functions. |
| TASK-003 | Starter seed function. |

**Wave:** 3

## Acceptance Criteria
- [ ] Fresh application startup creates schema and starter data before requests are served.
- [ ] Shutdown closes DB resources; test startup does not touch the developer's default DB.
- [ ] Initialization failures are logged and prevent serving a partially initialized app.

## Test Requirements
- **Unit tests:** Lifespan startup/shutdown invocation.
- **Integration tests:** Temporary database contains schema and starter courses after startup.
- **Edge cases:** Startup failure and repeated test-client lifespans.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-001 |
| Epic | EPIC-001 |
| BRD | BRD-FR-031–034, BRD-NFR-009, BRD-NFR-011 |

## Developer Agent Notes
`@4-develop-agent`: HLD section 8.1 and Database LLD sections 5–7. Wire only persistence lifecycle here; TASK-031 owns final feature-router registration.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
