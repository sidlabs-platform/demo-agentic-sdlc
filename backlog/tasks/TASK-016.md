# Task: Implement AI Request and Artifact Governance Service

| Field | Value |
|---|---|
| **Task ID** | TASK-016 |
| **Story** | STORY-007 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Wave**     | 2                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Orchestrate generation persistence, draft artifact creation, status updates, listing/retrieval, explicit approval metadata, and regeneration.

## Implementation Details
**Files to create/modify:** `src/ai/service.py`, `src/ai/models.py`, `tests/ai/test_service.py`.
**Approach:** Create ContentGenerationRequest before provider call; persist completed/failed state and a linked draft artifact; allow editing only while unapproved; record approver/time only on explicit approval. Regeneration creates a new request/artifact. Keep draft governance separate from course publishing and never auto-publish. The LLD does not define an artifact-to-lesson foreign key: do not invent one; keep unapproved artifacts ineligible for learner delivery and only offer approved content to Admin authoring.

## API Changes
N/A — handlers are TASK-017.

## Data Model Changes
Uses `content_generation_requests` and `content_generation_artifacts` from TASK-002.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Request/artifact persistence schema. |
| TASK-015 | Pluggable provider, prompt builders, and error types. |

**Wave:** 2

## Acceptance Criteria
- [ ] Each generation stores prompt/model/requester/status/time and linked draft content.
- [ ] Failures are marked failed with a user-safe retryable error and request context logged without key exposure.
- [ ] Draft content can be edited before approval; approve records Admin/time; regenerate creates new request/artifact; no automatic publication occurs.

## Test Requirements
- **Unit tests:** Generation success/failure, approval state, artifact filters, regeneration.
- **Integration tests:** Service against temporary SQLite with mocked provider.
- **Edge cases:** Missing/already-approved artifact, provider exception, repeated approval.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-007 |
| Epic | EPIC-004 |
| BRD | BRD-FR-028–030, BRD-INT-001–007, BRD-NFR-002, BRD-NFR-010, BRD-NFR-013–014 |

## Developer Agent Notes
`@4-develop-agent`: AI Generation LLD COMP-003 sections 2–6 and traceability section 9. BRD-FR-029 requires review/edit/approval; provide a draft edit operation that rejects already-approved artifacts. Artifact approval is not course publication; retain provenance and require explicit Admin action. NFR-002 follows synchronous MVP design (HLD DD-010) while measuring duration and returning a safe retryable result.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] External calls are mocked; no secret values appear in logs/errors
- [ ] Acceptance criteria verified
