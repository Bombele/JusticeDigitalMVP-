##############################################
# 📖 Guía detallada – infra-docs/
##############################################

## 1. Objetivo
La carpeta `infra-docs/` reúne toda la documentación institucional y técnica necesaria para:
- Garantizar el cumplimiento normativo (auditorías, certificaciones, gobernanza).
- Asegurar la trazabilidad (bitácoras trilingües).
- Proporcionar credibilidad institucional y preparar auditorías externas.

----------------------------------------------

## 2. Carpeta `infra-docs/compliance`
Esta carpeta contiene documentos normativos y de cumplimiento.

📂 infra-docs/compliance/
- kyc_kyb.md             → Procedimientos KYC/KYB (Know Your Customer / Know Your Business).
- sanctions_list.md      → Normalización de listas de sanciones.
- audit_requirements.md  → Checklist de auditoría institucional.
- certification_plan.md  → Plan de certificación ISO/IEC o equivalente.
- governance.md          → Reglas de gobernanza documental y técnica.

👉 **Buena práctica**:
- Cada archivo debe ser trilingüe (FR/ES/EN).
- Incluir referencias legales, normas locales e internacionales.
- Actualizar ante cada cambio regulatorio.

----------------------------------------------

## 3. Carpeta `infra-docs/bitacoras`
Esta carpeta contiene bitácoras trilingües para cada módulo.

📂 infra-docs/bitacoras/
- cache.md               → Bitácora del módulo cache.
- integrity.md           → Bitácora del módulo integridad.
- sync.md                → Bitácora del módulo sincronización.
- security.md            → Bitácora del módulo seguridad.
- observability.md       → Bitácora del módulo observabilidad.
- infra.md               → Bitácora de evoluciones técnicas (CI/CD, despliegue).

----------------------------------------------

## 4. Flujo documental
1. **Creación**: cada módulo comienza con un archivo mínimo de compliance + una bitácora vacía.
2. **Actualización**: añadir una entrada en la bitácora en cada commit o evolución.
3. **Auditabilidad**: alinear bitácoras con archivos de compliance.
4. **Institucionalización**: compliance = visión normativa, bitácoras = realidad operativa.

----------------------------------------------

## 5. Resultado esperado
- `infra-docs/compliance` → Normas y reglas institucionales.
- `infra-docs/bitacoras` → Diarios vivos y trazables.
- En conjunto → credibilidad, transparencia y preparación para auditoría externa.

----------------------------------------------

## 6. Conclusión / Síntesis
La carpeta `infra-docs/` constituye la **columna vertebral documental** del proyecto.  
- La sección **compliance** define reglas, estándares y requisitos institucionales.  
- La sección **bitácoras** registra la realidad diaria y la evolución técnica.  

En conjunto, garantizan una **trazabilidad completa**, una **credibilidad internacional** y una **preparación sólida para auditorías**.  
Este sistema documental convierte cada módulo técnico en un **activo institucional** listo para certificación y adopción externa.

##############################################