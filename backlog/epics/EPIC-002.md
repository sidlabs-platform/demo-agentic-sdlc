# Epic: Authentication and Authorization

| Field | Value |
|---|---|
| **Epic ID** | EPIC-002 |
| **Status** | Ready |
| **Owner** | Product / Engineering |
| **Created** | 2026-10-26 |
| **Target** | MVP |

## Goal / Objective
Allow Learners and Admins to register and sign in securely, and consistently enforce identity and role restrictions across protected endpoints.

## Business Value
Protects learner data and administrative authoring/reporting actions while giving both BRD personas access to the platform.

## BRD Requirements Mapped
| BRD ID | Description |
|---|---|
| BRD-FR-001–003 | Sign-in, role-based access, and registration |
| BRD-NFR-003–004 | Endpoint authorization and environment-only secrets |
| BRD-NFR-012 | Authentication event logging |

## Features
| Feature ID | Name | Priority | Status |
|---|---|---|---|
| FEAT-005 | Registration and login | P0 | Planned |
| FEAT-006 | JWT identity and role dependencies | P0 | Planned |

## Acceptance Criteria
1. Valid registration creates a user with a hashed password; duplicate email returns 409.
2. Valid credentials return a signed, expiring token; invalid credentials return 401.
3. Protected endpoints return 401 for missing/invalid identity and 403 when the role is insufficient; learner data is scoped to the authenticated user.

## Dependencies & Risks
**Dependencies:** EPIC-001 database and settings (COMP-007); Auth LLD COMP-001.
**Risks:** Signing secrets or password material must never be hardcoded, logged, or returned.

## Out of Scope
- OAuth/SSO, account recovery, and profile management beyond registration.

## Definition of Done
- [ ] All stories in this epic are Done
- [ ] Acceptance criteria verified
- [ ] Auth endpoints documented and tested
- [ ] No critical or high-severity bugs open
- [ ] Demo-ready for stakeholder review
