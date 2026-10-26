# Task: Expose Admin AI Generation and Artifact Routes

| Field | Value |
|---|---|
| **Task ID** | TASK-017 |
| **Story** | STORY-007 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 6h |
| **Wave**     | 3                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Expose the Admin-only AI generate, artifact list/get, draft edit, approve, and regenerate endpoints using TASK-016 service functions.

## Implementation Details
**Files to create/modify:** `src/ai/router.py`, `tests/ai/test_ai_api.py`.
**Approach:** Validate all inputs/outputs with AI LLD Pydantic models, inject auth and DB dependencies, map missing artifact/already-approved/provider errors to documented status codes and safe messages. Add the draft edit route because BRD-FR-029 explicitly requires review/edit; permit edits only before approval.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/ai/generate` | POST | Generate a lesson or quiz draft. |
| `/api/v1/ai/artifacts` | GET | List artifacts. |
| `/api/v1/ai/artifacts/{id}` | GET | Read artifact. |
| `/api/v1/ai/artifacts/{id}` | PUT | Edit unapproved draft content (BRD-FR-029). |
| `/api/v1/ai/artifacts/{id}/approve` | POST | Explicit Admin approval. |
| `/api/v1/ai/artifacts/{id}/regenerate` | POST | Regenerate as a new draft. |

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-007 | Admin authorization dependency. |
| TASK-016 | Generation and governance service. |

**Wave:** 3

## Acceptance Criteria
- [ ] All routes are Admin-only and return documented schemas/statuses; draft edits fail after approval.
- [ ] Provider failures return safe retryable response; secret data is absent.
- [ ] Artifact approve/regenerate operations preserve the draft governance lifecycle.

## Test Requirements
- **Unit tests:** N/A — service in TASK-016.
- **Integration tests:** Route success, validation, authorization, error mapping.
- **Edge cases:** Missing artifact, already approved, provider unavailable.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-007 |
| Epic | EPIC-004 |
| BRD | BRD-FR-028–030, BRD-INT-001–007, BRD-NFR-003, BRD-NFR-010, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: AI Generation LLD COMP-003 sections 2.2 and 4–6. `PUT /artifacts/{id}` is required by BRD-FR-029 but absent in the LLD; keep it narrow to unapproved generated content and document the extension. The router is mounted in TASK-031; route errors must not disclose internal provider responses or keys.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] API docs and route tests cover all handlers
- [ ] Acceptance criteria verified
