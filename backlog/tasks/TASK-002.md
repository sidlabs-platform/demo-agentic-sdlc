# Task: Implement SQLite Connection and Complete Schema

| Field | Value |
|---|---|
| **Task ID** | TASK-002 |
| **Story** | STORY-001 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Wave**     | 1                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement asynchronous SQLite connection management and the complete idempotent schema required by every service, including indexes, constraints, and foreign keys.

## Implementation Details
**Files to create/modify:**
- `src/database/__init__.py`, `src/database/connection.py` — `get_db()`, init/close lifecycle helpers.
- `src/database/schema.py` — CREATE TABLE/INDEX statements for users, courses, modules, lessons, quiz_questions, enrollments, progress_records, quiz_attempts, content_generation_requests, content_generation_artifacts.

**Approach:** Use aiosqlite and settings from TASK-001; set `row_factory`, enable `PRAGMA foreign_keys=ON`, use parameterized queries and `CREATE ... IF NOT EXISTS`. Preserve all columns/constraints in `LLD/database.md`.

## API Changes
N/A — database dependency only.

## Data Model Changes
Creates the ten entity tables and indexes described in `docs/design/LLD/database.md` sections 3 and 9.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-001 | Reads typed database path/settings. |

**Wave:** 1

## Acceptance Criteria
- [ ] All ten LLD tables and declared indexes/constraints exist on a new database.
- [ ] Foreign key checks are enabled for every request/startup connection.
- [ ] Repeated schema initialization is safe; connections close after use.

## Test Requirements
- **Unit tests:** Schema execution, foreign-key pragma, row mapping, connection cleanup.
- **Integration tests:** Initialize temporary DB, inspect tables/indexes, verify constraints.
- **Edge cases:** Repeated init and failed connection cleanup.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-001 |
| Epic | EPIC-001 |
| BRD | BRD-FR-023, BRD-FR-031–034, BRD-NFR-009, BRD-NFR-011 |

## Developer Agent Notes
`@4-develop-agent`: Follow Database LLD COMP-007 sections 2–3, 5–6. This is the shared persistence contract: keep table/column names consistent with each service LLD, use parameterized SQL, and do not implement business services in this task.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
