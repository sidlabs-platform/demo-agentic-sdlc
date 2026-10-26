# Epic: Learner and Admin Web Experience

| Field | Value |
|---|---|
| **Epic ID** | EPIC-007 |
| **Status** | Ready |
| **Owner** | Product / Engineering |
| **Created** | 2026-10-26 |
| **Target** | MVP |

## Goal / Objective
Deliver the BRD-defined Jinja2 pages and vanilla CSS/JavaScript interactions for Learners and Admins on desktop/tablet.

## Business Value
Makes the API capabilities usable through the minimal, responsive web experience required for the MVP.

## BRD Requirements Mapped
| BRD ID | Description |
|---|---|
| BRD-FR-003, BRD-FR-035–042 | Registration access and required Learner/Admin pages |
| BRD-NFR-005, BRD-NFR-007–008 | Safe lesson display, two-click navigation, responsive desktop/tablet |

## Features
| Feature ID | Name | Priority | Status |
|---|---|---|---|
| FEAT-019 | Shared layout and public auth pages | P0 | Planned |
| FEAT-020 | Learner discovery and study flow | P0 | Planned |
| FEAT-021 | Admin authoring, AI, and reports pages | P0 | Planned |

## Acceptance Criteria
1. All pages in Frontend LLD COMP-006 are rendered from Jinja2 templates and connect to their specified API endpoints.
2. Learners can navigate dashboard → course → lesson in at most two clicks and see sanitized content.
3. The layout works at desktop/tablet viewports (≥768px), with graceful narrow-screen behavior.

## Dependencies & Risks
**Dependencies:** EPIC-002 through EPIC-006 API contracts; Frontend LLD COMP-006.
**Risks:** Do not expose correct quiz answers or render unsanitized lesson HTML; retain vanilla JS/CSS/Jinja2 only.

## Out of Scope
- Native mobile applications, frontend frameworks, and mobile-specific UX beyond graceful layout degradation.

## Definition of Done
- [ ] All stories in this epic are Done
- [ ] Acceptance criteria verified
- [ ] Page/API flows and responsive behavior verified
- [ ] No critical or high-severity bugs open
- [ ] Demo-ready for stakeholder review
