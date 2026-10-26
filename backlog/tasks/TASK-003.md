# Task: Seed the Three Starter Courses

| Field | Value |
|---|---|
| **Task ID** | TASK-003 |
| **Story** | STORY-001 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 6h |
| **Wave**     | 2                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Add idempotent seed data for GitHub Foundations, GitHub Advanced Security, and GitHub Actions, including structured modules, Markdown lessons, and quizzes.

## Implementation Details
**Files to create/modify:**
- `src/database/seed.py` — course structures and `seed_starter_courses(db)`.
- `tests/database/test_seed.py` — seed requirements and idempotency.

**Approach:** Use the course/module/lesson outlines in `LLD/database.md` section 4. Match existing course names on repeat runs; each course must contain 3–5 modules, every module 1–3 lessons, and at least one quiz overall.

## API Changes
N/A.

## Data Model Changes
Populates `courses`, `modules`, `lessons`, and `quiz_questions`; no schema changes.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Requires initialized schema and aiosqlite connection. |

**Wave:** 2

## Acceptance Criteria
- [ ] All three named courses and valid structured content are seeded.
- [ ] Each course has at least one quiz question and meets the BRD module/lesson counts.
- [ ] Running seed repeatedly does not duplicate starter records.

## Test Requirements
- **Unit tests:** Data shape and course counts.
- **Integration tests:** Seed a fresh DB twice and verify exact course count and relations.
- **Edge cases:** Empty database and partially seeded database.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-001 |
| Epic | EPIC-001 |
| BRD | BRD-FR-031–034 |

## Developer Agent Notes
`@4-develop-agent`: Use COMP-007 `LLD/database.md` section 4 and COMP-002 `LLD/course-management.md` section 9.2. Keep seed logic data-only and deterministic; don't introduce extra course scope.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
