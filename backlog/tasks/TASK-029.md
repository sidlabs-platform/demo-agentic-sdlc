# Task: Build AI Generation and Artifact Review UI

| Field | Value |
|---|---|
| **Task ID** | TASK-029 |
| **Story** | STORY-016 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 7h |
| **Type / Agent** | Frontend — `@5-ui-develop-agent` |

## Description
Create the Admin generation form, editable artifact review/list view, explicit approval control, and regeneration interaction.

## Implementation Details
**Files to create/modify:**
- `src/templates/admin/generate.html`
- `src/static/css/admin-generate.css`, `src/static/js/admin-generate.js`
**Approach:** Use session/API helpers from TASK-024; collect topic, audience, objectives, difficulty, and output type; call Admin AI APIs; display editable draft/approved labels and safe errors. Approval is a deliberate user action; never expose provider credentials in client code.

## API Changes
Consumes AI generate, list/get/edit artifact, approve, and regenerate endpoints.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-024 | Shared page shell and session/API helpers. |
| TASK-017 | Admin AI generation/artifact API contract. |

**Wave:** 4

## Acceptance Criteria
- [ ] Form submits specified generation inputs and shows response content/status.
- [ ] Artifact list, draft editing, and approve/regenerate actions reflect returned state.
- [ ] Failure messages are useful and do not reveal provider details/secrets; no auto-publication.

## Test Requirements
- **Unit tests:** N/A — UI.
- **Integration tests:** Mock successful generation, draft edit, approval, regeneration, and failure responses.
- **Edge cases:** Empty input, long-running response, rate-limit error, missing artifact.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-016 |
| Epic | EPIC-007 |
| BRD | BRD-FR-041, BRD-FR-028–030, BRD-INT-001–006, BRD-NFR-010 |

## Developer Agent Notes
`@5-ui-develop-agent`: Frontend LLD COMP-006 sections 2.2 and 4.1; AI LLD COMP-003 sections 4 and 6. Use only browser-safe API responses; keep review/approval explicit.

## Definition of Done
- [ ] Generate, edit, review, approve, regenerate, and error states verified
- [ ] No provider secret is present in templates, JS, or logs
- [ ] Acceptance criteria verified
