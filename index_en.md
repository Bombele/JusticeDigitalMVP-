##############################################
# 📖 Index – Offline-first Project
##############################################

## 1. Project Root
📂 Offline-first/
- README.md              → General project overview.
- docs/                  → Institutional documentation and trilingual guides.
- infra_technical/       → Technical infrastructure (workflows, deployment, CI/CD).
- integrity-engine/      → Integrity engine (traceability, Merkle, signatures).
- observability-engine/  → Observability engine (metrics, logs, alerts).
- security-engine/       → Security engine (authentication, encryption, intrusion detection).
- sync-engine/           → Synchronization engine (offline-first, conflicts, cache).
- tests/                 → Test suite for each engine.

----------------------------------------------

## 2. Folder `infra_technical/`
📂 infra_technical/
- workflows/             → CI/CD workflows and monitoring.
- deployment/            → Docker/Kubernetes configurations.
- ci-cd/                 → Technical scripts (lint, coverage, deploy, monitor).

----------------------------------------------

## 3. Folder `integrity-engine/`
📂 integrity-engine/
- src/                   → Source code (append-only logs, Merkle, signatures).
- tests/                 → Unit and functional tests.
- docs/                  → Bitácoras and trilingual guides.
- infra/                 → CI/CD and deployment scripts.

----------------------------------------------

## 4. Folder `observability-engine/`
📂 observability-engine/
- src/                   → Source code (metrics, logs, alerts, dashboards).
- tests/                 → Unit and functional tests.
- infra/                 → CI/CD and deployment scripts.

----------------------------------------------

## 5. Folder `security-engine/`
📂 security-engine/
- src/                   → Source code (auth, encryption, intrusion detection).
- tests/                 → Unit and functional tests.
- docs/                  → Bitácoras, guides, compliance.
- infra/                 → CI/CD and deployment scripts.

----------------------------------------------

## 6. Folder `sync-engine/`
📂 sync-engine/
- src/                   → Source code (cache, sync worker, conflict resolver).
- tests/                 → Unit and functional tests.
- docs/                  → Bitácoras and practical guides.
- infra/                 → CI/CD and deployment scripts.

----------------------------------------------

## 7. Folder `tests/`
📂 tests/
- integrity_tests/       → Verifies append-only, Merkle, signatures.
- cache_tests/           → Verifies cache and queue management.
- security_tests/        → Verifies auth, encryption, detection.
- observability_tests/   → Verifies metrics, logs, alerts.
- sync_tests/            → Verifies synchronization and conflict resolution.

----------------------------------------------

## 8. Synthesis
The **Offline-first** project is structured into **specialized engines**:
- **Integrity Engine** → traceability and auditability.
- **Observability Engine** → supervision and transparency.
- **Security Engine** → protection and compliance.
- **Sync Engine** → offline-first continuity and conflict resolution.  

Supporting components:
- **infra_technical** → CI/CD automation and deployment.
- **tests** → complete and robust validation.  

Together, they form a **modular, auditable, and institutionally credible platform**, 
ready for adoption and certification.

##############################################