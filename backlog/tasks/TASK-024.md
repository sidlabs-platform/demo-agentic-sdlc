# Task: Build Shared Layout and Public Auth Pages

| Field | Value |
|---|---|
| **Task ID** | TASK-024 |
| **Story** | STORY-011 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 7h |
| **Wave**     | 3                 |
| **Type / Agent** | Frontend — `@5-ui-develop-agent` |

## Description
Build the shared Jinja2 layout and public login/register pages with responsive styling and browser interactions for the Auth API.

## Implementation Details
**Files to create/modify:**
- `src/templates/base.html`, `src/templates/components/nav.html`
- `src/templates/login.html`, `src/templates/register.html`
- `src/static/css/style.css`, `src/static/js/app.js`
**Approach:** Follow Frontend LLD COMP-006; use template inheritance, accessible form labels, inline validation/API error banners, and vanilla `fetch()`. Establish shared session/API helper functions in `app.js` for downstream pages. Store/send token only as described in Frontend LLD; do not embed secrets.

## API Changes
Consumes `POST /api/v1/auth/login` and `POST /api/v1/auth/register`.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-006 | Auth API contract and response behavior. |

**Wave:** 3

## Acceptance Criteria
- [ ] Login and registration templates extend shared base and submit to their API endpoints.
- [ ] Validation/authentication errors are visible and associated with the form.
- [ ] Shared navigation/layout is usable and responsive at viewports ≥768px.

## Test Requirements
- **Unit tests:** N/A — templates and browser interaction.
- **Integration tests:** Template rendering and auth form/API flow via frontend test approach.
- **Edge cases:** Invalid credentials, duplicate email, network failure, missing token.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-011 |
| Epic | EPIC-007 |
| BRD | BRD-FR-003, BRD-FR-035, BRD-NFR-008 |

## Developer Agent Notes
`@5-ui-develop-agent`: Frontend LLD COMP-006 sections 2–6. Vanilla HTML/CSS/JS and Jinja2 only; page route mounting is TASK-031. Use API responses rather than hardcoded user state.

## Definition of Done
- [ ] UI follows project conventions and is manually/automatically verified
- [ ] No console errors or unsafe content rendering
- [ ] Acceptance criteria verified
