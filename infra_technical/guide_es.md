##############################################
# 📖 Guía detallada – infra_technical/
##############################################

## 1. Objetivo
La carpeta `infra_technical/` reúne todos los componentes técnicos necesarios 
para automatizar, desplegar y supervisar el proyecto.  
Constituye la **columna vertebral operativa** que complementa la documentación institucional.

----------------------------------------------

## 2. Carpeta `infra_technical/workflows`
Esta carpeta contiene los flujos de integración y entrega continua.

📂 infra_technical/workflows/
- ci.yml              → Flujo CI (lint, pruebas, cobertura).
- cd.yml              → Flujo CD (despliegue automatizado).
- monitor.yml         → Flujo de monitoreo y alertas.
- rollback.yml        → Procedimiento de rollback en caso de fallo.

👉 **Buena práctica**:
- Definir jobs separados (lint, test, build, deploy).
- Usar secretos seguros para credenciales.
- Añadir notificaciones (Slack, email) en caso de fallo.

----------------------------------------------

## 3. Carpeta `infra_technical/deployment`
Esta carpeta contiene las configuraciones de despliegue.

📂 infra_technical/deployment/
- docker-compose.yml  → Despliegue local con Docker.
- k8s-deployment.yaml → Despliegue en Kubernetes (pods, servicios).
- monitoring-config.yml → Configuración Prometheus/Grafana.
- env.example         → Ejemplo de variables de entorno.

👉 **Buena práctica**:
- Separar entornos (dev, staging, prod).
- Documentar cada parámetro en `env.example`.
- Validar compatibilidad con CI/CD antes de producción.

----------------------------------------------

## 4. Carpeta `infra_technical/ci-cd`
Esta carpeta contiene scripts y herramientas para CI/CD.

📂 infra_technical/ci-cd/
- lint.sh             → Verificación de calidad de código.
- coverage.sh         → Medición de cobertura de pruebas.
- deploy.sh           → Script de despliegue automatizado.
- monitor.sh          → Verificación de disponibilidad de servicios.
- cleanup.sh          → Limpieza de recursos tras rollback.

👉 **Buena práctica**:
- Scripts modulares y reutilizables.
- Incluir logs y códigos de retorno claros.
- Probar cada script de forma independiente antes de integrarlo en workflows.

----------------------------------------------

## 5. Flujo técnico global
1. **Desarrollo**: commit en rama feature → dispara CI (lint + pruebas).
2. **Integración**: merge en `develop` → dispara build + cobertura.
3. **Despliegue**: merge en `main` → dispara CD (Docker/K8s).
4. **Monitoreo**: workflows + scripts supervisan disponibilidad y alertas.
5. **Rollback**: en caso de fallo, ejecución automática de `rollback.yml` + `cleanup.sh`.

----------------------------------------------

## 6. Resultado esperado
- `workflows` → Automatización CI/CD y monitoreo.
- `deployment` → Configuraciones Docker/Kubernetes.
- `ci-cd` → Scripts técnicos modulares.  
En conjunto → un **sistema técnico robusto**, auditable y listo para producción.

----------------------------------------------

## 7. Conclusión / Síntesis
La carpeta `infra_technical/` es la **columna vertebral operativa** del proyecto.  
- Los **workflows** aseguran automatización y fiabilidad.  
- El **deployment** garantiza portabilidad y escalabilidad.  
- Los **scripts CI/CD** proporcionan herramientas prácticas para ejecución y supervisión.  

En conjunto, ofrecen una **infraestructura técnica completa**, capaz de sostener 
la evolución del proyecto, superar auditorías y facilitar la adopción por socios externos.

##############################################