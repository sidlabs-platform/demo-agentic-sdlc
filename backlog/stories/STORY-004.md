# Story: Manage Course Lifecycle and Discovery API

| Field | Value |
|---|---|
| **Story ID** | STORY-004 |
| **Epic** | EPIC-003 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | L |
| **Priority** | P0 |

## User Story
**As an** Admin or Learner, **I want** course lifecycle and discovery endpoints, **so that** Admins can manage offerings and Learners can find available courses.

## Acceptance Criteria
1. **Given** an Admin creates or updates a course, **When** valid data is submitted, **Then** persisted metadata is returned and new courses start as drafts.
2. **Given** a course is published/unpublished/deleted, **When** the Admin invokes the lifecycle endpoint, **Then** content rules, cascade behavior, and existing-enrollment preservation match the BRD.
3. **Given** a Learner lists courses, **When** the catalog is requested, **Then** only published courses are returned; detail includes ordered modules and lesson summaries.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-004–010 | COMP-002, `LLD/course-management.md` |
| BRD-NFR-001, BRD-NFR-003, BRD-NFR-011, BRD-NFR-015–017 | COMP-002 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-008 | Implement course schemas and lifecycle/query services | 8h |
| TASK-009 | Expose course CRUD, lifecycle, catalog, and detail routes | 8h |

## UI/UX Notes
Admin and Learner page interactions are covered by STORY-013 and STORY-016.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, aiosqlite.
- **Key considerations:** Admin role on mutations; role-aware list/detail; course publish requires modules and lessons.
- **Configuration:** Shared database settings.

## Dependencies
- TASK-002 schema; TASK-007 RBAC before route handlers.

## Definition of Done
- [ ] Every endpoint and service branch has pytest coverage
- [ ] API responses use Pydantic v2 schemas
- [ ] No regressions in existing tests
