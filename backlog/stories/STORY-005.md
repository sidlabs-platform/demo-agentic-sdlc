# Story: Author Modules and Lessons

| Field | Value |
|---|---|
| **Story ID** | STORY-005 |
| **Epic** | EPIC-003 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | L |
| **Priority** | P0 |

## User Story
**As an** Admin, **I want** to create, update, and delete modules and lessons, **so that** course content is structured and maintained.

## Acceptance Criteria
1. **Given** a valid course/module, **When** an Admin creates or updates a module or lesson, **Then** ordered metadata and Markdown content persist.
2. **Given** an Admin deletes a module, **When** it has lessons or quizzes, **Then** child records are removed consistently.
3. **Given** a Learner requests lesson content, **When** Markdown is rendered, **Then** returned HTML is sanitized against script/event-handler XSS.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-011–015 | COMP-002, `LLD/course-management.md` |
| BRD-NFR-003, BRD-NFR-005, BRD-NFR-015–017 | COMP-002 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-010 | Implement module and lesson schemas/services | 8h |
| TASK-011 | Expose Admin module and lesson CRUD routes | 6h |
| TASK-012 | Implement Markdown rendering and sanitization | 4h |
| TASK-013 | Expose sanitized lesson retrieval | 4h |

## UI/UX Notes
Admin editor and Learner lesson page are covered by STORY-016 and STORY-014.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, aiosqlite, Markdown renderer, bleach or nh3.
- **Key considerations:** Preserve sort order; sanitize after Markdown conversion; keep the sanitizer isolated/swappable.
- **Configuration:** Shared database settings.

## Dependencies
- TASK-010 depends on TASK-002 and course service TASK-008; routes depend on TASK-007. Sanitized retrieval depends on TASK-012.

## Definition of Done
- [ ] CRUD, cascade, validation, and hostile-Markdown cases are tested
- [ ] Learner response never includes unsanitized HTML
- [ ] No regressions in existing tests
