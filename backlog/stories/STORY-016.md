# Story: Generate and Review AI Content from the Admin UI

| Field | Value |
|---|---|
| **Story ID** | STORY-016 |
| **Epic** | EPIC-007 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P0 |

## User Story
**As an** Admin, **I want** a page to generate and review AI artifacts, **so that** I can use AI assistance while retaining approval control.

## Acceptance Criteria
1. **Given** generation inputs, **When** submitted, **Then** the page displays returned content and status.
2. **Given** a draft artifact, **When** an Admin edits, approves, or regenerates it, **Then** the corresponding API action is used and approval state is visible.
3. **Given** generation fails, **When** the error is returned, **Then** a safe retryable message is displayed without sensitive configuration.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-041, BRD-FR-028–030 | COMP-006/003 |
| BRD-INT-001–006, BRD-NFR-008, BRD-NFR-010 | COMP-003/006 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-029 | Build AI generation and artifact review UI | 7h |

## UI/UX Notes
Provide topic, audience, objectives, difficulty, output type, artifact list, and clear draft/approved labels.

## Technical Notes
- **Stack:** Jinja2, CSS, vanilla JS.
- **Key considerations:** Admin-only page; call AI API; never expose API key; approval is explicit.
- **Configuration:** No browser-side AI credentials.

## Dependencies
- AI routes TASK-017 and page route integration TASK-031.

## Definition of Done
- [ ] Generate/list/approve/regenerate flows and safe failure messages are verified
- [ ] Draft content is never presented as published automatically
