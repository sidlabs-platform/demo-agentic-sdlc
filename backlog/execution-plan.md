# Execution Plan

Generated from `backlog/dependency-graph.json` by the build-planner workflow.

**Total waves**: 8  
**Total tasks**: 31  
**Backend tasks**: 24  
**Frontend tasks**: 7  

## Wave 0 — Foundation (no dependencies)
**Branch:** `wave-0/foundation`

### Backend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-001 | Add Application Settings and FastAPI Foundation | — |

### Frontend Tasks
_None in this wave_

---

## Wave 1 — Core infrastructure (Wave 0)
**Branch:** `wave-1/core-infrastructure`

### Backend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-002 | Implement SQLite Connection and Complete Schema | TASK-001 |
| TASK-005 | Define Auth Schemas and Security Utilities | TASK-001 |
| TASK-012 | Implement Markdown Rendering and XSS Sanitization | TASK-001 |
| TASK-015 | Build Pluggable GitHub Models Client and Prompts | TASK-001 |

### Frontend Tasks
_None in this wave_

---

## Wave 2 — Persistence and service foundations (Wave 0, Wave 1)
**Branch:** `wave-2/persistence-and-service-foundations`

### Backend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-003 | Seed the Three Starter Courses | TASK-002 |
| TASK-006 | Implement Registration and Login APIs | TASK-002, TASK-005 |
| TASK-007 | Implement Current-User and Role Dependencies | TASK-002, TASK-005 |
| TASK-008 | Implement Course Schemas and Lifecycle Services | TASK-002 |
| TASK-016 | Implement AI Request and Artifact Governance Service | TASK-002, TASK-015 |
| TASK-022 | Implement Reporting Models and Read-Only Service | TASK-002 |

### Frontend Tasks
_None in this wave_

---

## Wave 3 — Service APIs and public shell (Wave 0, Wave 1, Wave 2)
**Branch:** `wave-3/service-apis-and-public-shell`

### Backend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-004 | Initialize Persistence During Application Lifespan | TASK-001, TASK-002, TASK-003 |
| TASK-009 | Expose Course Lifecycle and Discovery Routes | TASK-007, TASK-008 |
| TASK-010 | Implement Module and Lesson Services | TASK-002, TASK-008 |
| TASK-017 | Expose Admin AI Generation and Artifact Routes | TASK-007, TASK-016 |
| TASK-018 | Implement Learner Enrollment Service | TASK-002, TASK-007, TASK-008 |
| TASK-023 | Expose Admin Reporting Endpoints | TASK-007, TASK-022 |

### Frontend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-024 | Build Shared Layout and Public Auth Pages | TASK-006 |

---

## Wave 4 — Feature endpoints and first Admin UI (Wave 0, Wave 1, Wave 2, Wave 3)
**Branch:** `wave-4/feature-endpoints-and-first-admin-ui`

### Backend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-011 | Expose Admin Module and Lesson CRUD Routes | TASK-007, TASK-010 |
| TASK-013 | Expose Sanitized Lesson Retrieval | TASK-007, TASK-010, TASK-012 |
| TASK-014 | Implement Quiz Authoring and Attempt APIs | TASK-002, TASK-007, TASK-010 |
| TASK-019 | Expose Learner Enrollment Route | TASK-007, TASK-018 |
| TASK-020 | Implement Transactional Lesson Progress Updates | TASK-002, TASK-007, TASK-010, TASK-018 |

### Frontend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-029 | Build AI Generation and Artifact Review UI | TASK-017, TASK-024 |
| TASK-030 | Build Admin Reports Dashboard UI | TASK-023, TASK-024 |

---

## Wave 5 — Learner progress API and learner/authoring pages (Wave 0, Wave 1, Wave 2, Wave 3, Wave 4)
**Branch:** `wave-5/learner-progress-api-and-learner-authoring-pages`

### Backend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-021 | Implement Learner Enrollment and Progress Dashboard API | TASK-007, TASK-018, TASK-020 |

### Frontend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-025 | Build Course Catalog and Detail Pages | TASK-009, TASK-019, TASK-024 |
| TASK-026 | Build Lesson Viewer and Quiz Interactions | TASK-013, TASK-014, TASK-020, TASK-024 |
| TASK-028 | Build Admin Course and Content Management UI | TASK-009, TASK-011, TASK-013, TASK-014, TASK-024 |

---

## Wave 6 — Learner dashboard experience (Wave 0, Wave 1, Wave 2, Wave 3, Wave 4, Wave 5)
**Branch:** `wave-6/learner-dashboard-experience`

### Backend Tasks
_None in this wave_

### Frontend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-027 | Build Learner Dashboard and Progress UI | TASK-021, TASK-024 |

---

## Wave 7 — Final application route assembly and integration checks (Wave 0, Wave 1, Wave 2, Wave 3, Wave 4, Wave 5, Wave 6)
**Branch:** `wave-7/final-application-route-assembly-and-integration-checks`

### Backend Tasks
| Task ID  | Title | Dependencies |
|----------|-------|--------------|
| TASK-031 | Wire Feature APIs and Frontend Page Routes | TASK-001, TASK-004, TASK-006, TASK-009, TASK-011, TASK-013, TASK-014, TASK-017, TASK-019, TASK-020, TASK-021, TASK-023, TASK-024, TASK-025, TASK-026, TASK-027, TASK-028, TASK-029, TASK-030 |

### Frontend Tasks
_None in this wave_

---
