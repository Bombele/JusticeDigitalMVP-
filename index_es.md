##############################################
# 📖 Índice – Proyecto Offline-first
##############################################

## 1. Raíz del proyecto
📂 Offline-first/
- README.md              → Presentación general del proyecto.
- docs/                  → Documentación institucional y guías trilingües.
- infra_technical/       → Infraestructura técnica (workflows, despliegue, CI/CD).
- integrity-engine/      → Motor de integridad (trazabilidad, Merkle, firmas).
- observability-engine/  → Motor de observabilidad (métricas, logs, alertas).
- security-engine/       → Motor de seguridad (autenticación, cifrado, detección).
- sync-engine/           → Motor de sincronización (offline-first, conflictos, caché).
- tests/                 → Suite de pruebas para cada motor.

----------------------------------------------

## 2. Carpeta `infra_technical/`
📂 infra_technical/
- workflows/             → Workflows CI/CD y monitoreo.
- deployment/            → Configuraciones Docker/Kubernetes.
- ci-cd/                 → Scripts técnicos (lint, coverage, deploy, monitor).

----------------------------------------------

## 3. Carpeta `integrity-engine/`
📂 integrity-engine/
- src/                   → Código fuente (append-only logs, Merkle, firmas).
- tests/                 → Pruebas unitarias y funcionales.
- docs/                  → Bitácoras y guías trilingües.
- infra/                 → CI/CD y scripts de despliegue.

----------------------------------------------

## 4. Carpeta `observability-engine/`
📂 observability-engine/
- src/                   → Código fuente (métricas, logs, alertas, dashboards).
- tests/                 → Pruebas unitarias y funcionales.
- infra/                 → CI/CD y scripts de despliegue.

----------------------------------------------

## 5. Carpeta `security-engine/`
📂 security-engine/
- src/                   → Código fuente (auth, cifrado, detección de intrusiones).
- tests/                 → Pruebas unitarias y funcionales.
- docs/                  → Bitácoras, guías, cumplimiento.
- infra/                 → CI/CD y scripts de despliegue.

----------------------------------------------

## 6. Carpeta `sync-engine/`
📂 sync-engine/
- src/                   → Código fuente (caché, sync worker, conflict resolver).
- tests/                 → Pruebas unitarias y funcionales.
- docs/                  → Bitácoras y guías prácticas.
- infra/                 → CI/CD y scripts de despliegue.

----------------------------------------------

## 7. Carpeta `tests/`
📂 tests/
- integrity_tests/       → Verifica append-only, Merkle, firmas.
- cache_tests/           → Verifica gestión de caché y colas.
- security_tests/        → Verifica auth, cifrado, detección.
- observability_tests/   → Verifica métricas, logs, alertas.
- sync_tests/            → Verifica sincronización y resolución de conflictos.

----------------------------------------------

## 8. Síntesis
El proyecto **Offline-first** está estructurado en **motores especializados**:
- **Integrity Engine** → trazabilidad y auditabilidad.
- **Observability Engine** → supervisión y transparencia.
- **Security Engine** → protección y cumplimiento.
- **Sync Engine** → continuidad offline-first y resolución de conflictos.  

Componentes de soporte:
- **infra_technical** → automatización CI/CD y despliegue.
- **tests** → validación completa y robusta.  

En conjunto, forman una **plataforma modular, auditable y con credibilidad institucional**, 
lista para adopción y certificación.

##############################################