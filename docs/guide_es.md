##############################################
# 📖 Guía detallada – Carpetas institucionales
##############################################

## 1. Objetivo
Las carpetas `docs/guides` y `docs/bitacora` están diseñadas para:
- Garantizar la trazabilidad documental (bitácoras).
- Proporcionar guías prácticas para uso, despliegue y auditorías.
- Establecer credibilidad institucional desde las primeras etapas del proyecto.

----------------------------------------------

## 2. Carpeta `docs/guides`
Esta carpeta contiene **documentos prácticos** para usuarios, socios y auditores.

📂 docs/guides/
- deployment.md        → Guía de despliegue (Docker, Kubernetes, CI/CD).
- compliance.md        → Normas de cumplimiento (KYC/KYB, sanciones, certificación).
- audit.md             → Procedimientos de auditoría y checklist institucional.
- cache_usage.md       → Guía específica del módulo cache.
- integrity_usage.md   → Guía específica del módulo integridad.
- sync_usage.md        → Guía específica del módulo sincronización.
- security_usage.md    → Guía específica del módulo seguridad.
- observability_usage.md → Guía específica del módulo observabilidad.

👉 **Buena práctica**: cada guía debe ser trilingüe (FR/ES/EN) e incluir:
- Objetivo del módulo o procedimiento.
- Pasos prácticos.
- Notas institucionales (auditoría, cumplimiento).
- Ejemplo mínimo (código o flujo de trabajo).

----------------------------------------------

## 3. Carpeta `docs/bitacora`
Esta carpeta contiene **bitácoras trilingües** para cada módulo.

📂 docs/bitacora/
- cache.md             → Bitácora del módulo cache.
- integrity.md         → Bitácora del módulo integridad.
- sync.md              → Bitácora del módulo sincronización.
- security.md          → Bitácora del módulo seguridad.
- observability.md     → Bitácora del módulo observabilidad.

👉 **Buena práctica**: cada bitácora debe seguir el formato: