# Story: Establish the Application and Persistence Foundation

| Field | Value |
|---|---|
| **Story ID** | STORY-001 |
| **Epic** | EPIC-001 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | L |
| **Priority** | P0 |

## User Story
**As a** Platform Admin, **I want** the platform initialized with its shared configuration, database, and starter learning content, **so that** all workflows have a reliable foundation.

## Acceptance Criteria
1. **Given** valid environment settings, **When** the app starts, **Then** it loads settings without source-code secrets and applies configured CORS.
2. **Given** a fresh SQLite file, **When** initialization runs, **Then** all LLD tables/indexes are created and foreign keys enforced.
3. **Given** initialization runs more than once, **When** seed data is applied, **Then** each of the three named courses has 3–5 modules, 1–3 lessons per module, and at least one quiz, without duplicate seed records.
4. **Given** all feature routers and templates exist, **When** the app is assembled, **Then** their API and HTML routes are reachable.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-023, BRD-FR-031–034 | COMP-007, `LLD/database.md` |
| BRD-NFR-001, 004, 006, 009, 011, 015–017 | COMP-007 / application foundation |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-001 | Add settings and FastAPI app foundation | 6h |
| TASK-002 | Implement SQLite connection and complete schema | 8h |
| TASK-003 | Seed the three starter courses idempotently | 6h |
| TASK-004 | Initialize DB and seed data through app lifespan | 3h |
| TASK-031 | Register all delivered API and frontend routers | 4h |

## UI/UX Notes
N/A — platform foundation.

## Technical Notes
- **Stack:** Python 3.11+, FastAPI, Pydantic Settings, SQLite, aiosqlite.
- **Key considerations:** Follow database LLD schema, enforce SQLite foreign keys, initialize idempotently.
- **Configuration:** `DATABASE_URL`, `SECRET_KEY`, `CORS_ALLOWED_ORIGINS`; AI settings are consumed by COMP-003.

## Dependencies
- TASK-001 precedes persistence; TASK-002 precedes seed/startup; TASK-031 waits for all API/page route modules.

## Definition of Done
- [ ] Acceptance criteria verified and tests pass on a fresh temporary DB
- [ ] Settings, database, seed, and route assembly follow project conventions
- [ ] No regressions in existing tests
