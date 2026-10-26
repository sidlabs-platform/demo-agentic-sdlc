# Story: Generate and Govern AI Draft Content

| Field | Value |
|---|---|
| **Story ID** | STORY-007 |
| **Epic** | EPIC-004 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | XL |
| **Priority** | P0 |

## User Story
**As an** Admin, **I want** to generate, review, approve, and regenerate AI content, **so that** course authoring is faster without bypassing human review.

## Acceptance Criteria
1. **Given** configured GitHub Models access, **When** an Admin requests lesson/quiz generation, **Then** a request record and linked draft artifact are created with audit metadata.
2. **Given** a transient 429/5xx failure, **When** a generation call fails, **Then** bounded exponential retries run and a safe, retryable status is returned after exhaustion.
3. **Given** an artifact is unapproved, **When** it is reviewed or regenerated, **Then** it remains draft/AI-labeled until explicit Admin approval; regeneration creates a new request/artifact.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-028–030, BRD-INT-001–007 | COMP-003, `LLD/ai-generation.md` |
| BRD-NFR-002, BRD-NFR-004, BRD-NFR-010, BRD-NFR-013–014 | COMP-003 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-015 | Build provider protocol, prompts, and GitHub Models client | 8h |
| TASK-016 | Implement request/artifact generation and governance service | 8h |
| TASK-017 | Expose Admin generation, artifacts, approval, and regeneration routes | 6h |

## UI/UX Notes
Admin generation/review UI is covered by STORY-017.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, httpx, aiosqlite.
- **Key considerations:** GPT-4o default; API key from environment; 429/5xx retry with bounded backoff; never auto-publish or expose key.
- **Configuration:** `GITHUB_MODELS_API_KEY`, `GITHUB_MODELS_ENDPOINT`, `AI_MODEL_NAME`, `AI_MAX_RETRIES`, `AI_REQUEST_TIMEOUT_SECONDS`.

## Dependencies
- TASK-015 requires shared settings TASK-001; TASK-016 requires storage TASK-002; TASK-017 requires TASK-007 and TASK-016.

## Definition of Done
- [ ] Provider calls mocked in unit/integration tests
- [ ] Retry, safe error, audit metadata, approve, and regenerate criteria verified
- [ ] No regressions in existing tests
