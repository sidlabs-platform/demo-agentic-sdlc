# Task: Implement Markdown Rendering and XSS Sanitization

| Field | Value |
|---|---|
| **Task ID** | TASK-012 |
| **Story** | STORY-005 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 4h |
| **Wave**     | 1                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Create an isolated renderer that converts lesson Markdown into HTML and sanitizes executable tags, event handlers, and unsafe attributes.

## Implementation Details
**Files to create/modify:** `src/courses/sanitizer.py`, `tests/courses/test_sanitizer.py`, dependency declarations if required.
**Approach:** Use the Markdown and established sanitizer option selected by HLD DD-007; allow only safe markup and links. Do not use regular expressions as the security boundary.

## API Changes
N/A — utility consumed by TASK-013.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-001 | Shared project dependency configuration. |

**Wave:** 1

## Acceptance Criteria
- [ ] Markdown is converted to useful HTML and output is sanitized using an established library.
- [ ] Script tags, event-handler attributes, and dangerous URL schemes are removed.
- [ ] Renderer has a typed public function and remains isolated behind `render_and_sanitize_markdown()`.

## Test Requirements
- **Unit tests:** Safe Markdown formatting and sanitization allowlist.
- **Integration tests:** N/A — lesson API tests in TASK-013.
- **Edge cases:** Nested tags, malformed markup, encoded dangerous URLs, raw HTML.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-005 |
| Epic | EPIC-003 |
| BRD | BRD-FR-015, BRD-NFR-005, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Course Management LLD COMP-002 sections 2.2, 2.3, 5.2, and 8; HLD DD-007. Keep this code isolated and avoid new sanitizer implementations.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
