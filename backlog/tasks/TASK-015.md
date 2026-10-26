# Task: Build Pluggable GitHub Models Client and Prompts

| Field | Value |
|---|---|
| **Task ID** | TASK-015 |
| **Story** | STORY-007 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Wave**     | 1                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement the provider protocol, lesson/quiz prompt builders, and async GitHub Models HTTP client with bounded exponential retry.

## Implementation Details
**Files to create/modify:** `src/ai/__init__.py`, `src/ai/interface.py`, `src/ai/client.py`, `src/ai/prompts.py`, `src/ai/models.py`, `tests/ai/test_client.py`, `tests/ai/test_prompts.py`.
**Approach:** Follow AI LLD COMP-003; use httpx and settings, default model `gpt-4o`, retry 429/5xx up to configured max with backoff/jitter, and expose a protocol for alternate providers. Do not log key or raw secret-bearing headers.

## API Changes
N/A — provider client and data schemas only.

## Data Model Changes
N/A — persistence in TASK-016.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-001 | Reads typed AI endpoint/key/model/retry/timeout settings. |

**Wave:** 1

## Acceptance Criteria
- [ ] Protocol can be implemented by provider alternatives without changing service logic.
- [ ] Lesson and quiz prompt builders use requested learning inputs/output type.
- [ ] 429/5xx retry behavior is bounded/configurable; API key is never logged or returned.

## Test Requirements
- **Unit tests:** Prompt construction, response parsing, retry counts and delays with mocked httpx.
- **Integration tests:** N/A — service integration in TASK-016/017.
- **Edge cases:** Timeout, malformed provider response, exhausted retries, non-retryable status.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-007 |
| Epic | EPIC-004 |
| BRD | BRD-INT-001, BRD-INT-004, BRD-INT-007, BRD-NFR-004 |

## Developer Agent Notes
`@4-develop-agent`: AI Generation LLD COMP-003 sections 2, 5–8. Use `ContentGeneratorProtocol`, async httpx, dependency injection, and safe exception types; published content must not call this client at read time.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] Provider calls are fully mocked in tests
- [ ] Acceptance criteria verified
