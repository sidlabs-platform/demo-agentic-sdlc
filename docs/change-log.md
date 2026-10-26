# Change Log

All notable decisions and changes for the AI-Powered Learning Platform are documented here.

---

## [2026-10-26] — SDLC Stage 3 Backlog Decomposition

**Author:** 3-epic-and-tasks-agent
**Artifacts:** `backlog/epics/`, `backlog/stories/`, `backlog/tasks/`, `backlog/dependency-graph.json`

**Summary:**
Created 7 traceable EPICs, 17 user stories, and 31 implementation tasks (24 backend and 7 frontend) from the BRD, HLD, component LLDs, project conventions, and supplied templates. The dependency manifest includes wave assignments and a directed acyclic prerequisite graph for backend and frontend work.

**Key Delivery Decisions:**
- Decomposed the work along the seven HLD component boundaries, grouping UI flows under the frontend epic and shared persistence/startup under the foundation epic.
- Added a draft-artifact edit operation to the AI API task because BRD-FR-029 requires Admin review and editing, while the current AI LLD specifies approval but no edit endpoint. The task documents this narrow API extension.
- Kept artifact approval separate from course publication and preserved the LLD's synchronous MVP generation choice; generated content is never auto-published.
- Defined application-router assembly as the final dependency wave so route registration consumes the completed API modules and page assets.

**Traceability:** Every Epic maps to BRD requirement IDs; each Story maps to one Epic and BRD/HLD/LLD references; every Task lists its parent Story/Epic, BRD IDs, prerequisites, implementation files, agent, and tests. The graph has 31 tasks across waves 0–7.

---

## [2026-04-22] — High-Level and Low-Level Design Created

**Author:** 2-plan-and-design-agent  
**Artifacts:** `docs/design/HLD.md`, `docs/design/LLD/*.md`

**Summary:**  
Created the High-Level Design (HLD) and Low-Level Design (LLD) documents for the AI-Powered Learning Platform MVP. The HLD defines the system architecture with 7 components: Auth Service (COMP-001), Course Management Service (COMP-002), AI Generation Service (COMP-003), Progress Tracking Service (COMP-004), Reporting Service (COMP-005), Frontend UI Layer (COMP-006), and Database Layer (COMP-007). The architecture follows a monolithic FastAPI application with feature-based module organization, SQLite database, Jinja2 server-rendered frontend, and a pluggable GitHub Models API integration.

**Key Design Decisions:**
- DD-001: SQLite for MVP database (zero-config, file-based)
- DD-002: Jinja2 server-side rendering (no frontend framework)
- DD-003: JWT tokens for stateless authentication
- DD-004: Pluggable AI service module behind Protocol/ABC interface
- DD-005: bcrypt for password hashing
- DD-006: aiosqlite for async database access
- DD-007: bleach/nh3 for XSS sanitization of Markdown content
- DD-008: URL-prefix API versioning (/api/v1/)
- DD-009: Feature-based folder organization under src/
- DD-010: Synchronous AI generation for MVP (evolvable to async)

**LLD Documents:**
- `docs/design/LLD/auth.md` — Auth Service (COMP-001): Registration, login, JWT, RBAC
- `docs/design/LLD/course-management.md` — Course Management (COMP-002): CRUD, publish/unpublish, sanitization
- `docs/design/LLD/ai-generation.md` — AI Generation (COMP-003): GitHub Models integration, prompts, retry logic
- `docs/design/LLD/progress-tracking.md` — Progress Tracking (COMP-004): Enrollment, completion, auto-progress
- `docs/design/LLD/reporting.md` — Reporting (COMP-005): Dashboard stats, per-learner progress, CSV export
- `docs/design/LLD/frontend.md` — Frontend (COMP-006): Jinja2 templates, responsive CSS, 2-click navigation
- `docs/design/LLD/database.md` — Database Layer (COMP-007): Complete schema, seed data, connection management

**Traceability:** All design elements trace back to BRD requirement IDs (BRD-FR-*, BRD-NFR-*, BRD-INT-*). Full traceability matrix in HLD Section 11.

---

## [2026-04-22] — BRD Created

**Author:** 1-requirement-agent  
**Artifacts:** `docs/requirements/BRD.md`

**Summary:**  
Created the initial Business Requirements Document (BRD) for the AI-Powered Learning Platform MVP. The BRD defines 42 functional requirements, 17 non-functional requirements, and 7 integration requirements covering authentication, course management, module/lesson CRUD, quiz functionality, enrollment and progress tracking, AI content generation via GitHub Models API (GPT-4o), content governance (draft → review → publish), admin reporting, frontend pages, and three starter courses (GitHub Foundations, GitHub Advanced Security, GitHub Actions). Requirements were derived from the project copilot-instructions.md and the issue context. All requirements have unique IDs (BRD-FR-*, BRD-NFR-*, BRD-INT-*) for traceability by downstream agents.
