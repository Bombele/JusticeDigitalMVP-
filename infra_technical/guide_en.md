##############################################
# 📖 Detailed Guide – infra_technical/
##############################################

## 1. Objective
The `infra_technical/` folder consolidates all technical components required 
to automate, deploy, and monitor the project.  
It serves as the **operational backbone** complementing institutional documentation.

----------------------------------------------

## 2. Folder `infra_technical/workflows`
This folder contains integration and delivery workflows.

📂 infra_technical/workflows/
- ci.yml              → CI workflow (lint, tests, coverage).
- cd.yml              → CD workflow (automated deployment).
- monitor.yml         → Monitoring and alert workflow.
- rollback.yml        → Rollback procedure in case of failure.

👉 **Best practice**:
- Define separate jobs (lint, test, build, deploy).
- Use secure secrets for credentials.
- Add notifications (Slack, email) on failure.

----------------------------------------------

## 3. Folder `infra_technical/deployment`
This folder contains deployment configurations.

📂 infra_technical/deployment/
- docker-compose.yml  → Local deployment with Docker.
- k8s-deployment.yaml → Kubernetes deployment (pods, services).
- monitoring-config.yml → Prometheus/Grafana monitoring configuration.
- env.example         → Example environment variables.

👉 **Best practice**:
- Separate environments (dev, staging, prod).
- Document each parameter in `env.example`.
- Validate compatibility with CI/CD before production release.

----------------------------------------------

## 4. Folder `infra_technical/ci-cd`
This folder contains scripts and tools for CI/CD.

📂 infra_technical/ci-cd/
- lint.sh             → Code quality check.
- coverage.sh         → Test coverage measurement.
- deploy.sh           → Automated deployment script.
- monitor.sh          → Service availability check.
- cleanup.sh          → Resource cleanup after rollback.

👉 **Best practice**:
- Modular and reusable scripts.
- Include clear logs and return codes.
- Test each script independently before workflow integration.

----------------------------------------------

## 5. Global Technical Workflow
1. **Development**: commit on feature branch → triggers CI (lint + tests).
2. **Integration**: merge into `develop` → triggers build + coverage.
3. **Deployment**: merge into `main` → triggers CD (Docker/K8s).
4. **Monitoring**: workflows + scripts supervise availability and alerts.
5. **Rollback**: on failure, automatic execution of `rollback.yml` + `cleanup.sh`.

----------------------------------------------

## 6. Expected Outcome
- `workflows` → CI/CD automation and monitoring.
- `deployment` → Docker/Kubernetes configurations.
- `ci-cd` → Practical modular scripts.  
Together → a **robust technical system**, auditable and production-ready.

----------------------------------------------

## 7. Conclusion / Synthesis
The `infra_technical/` folder is the **operational backbone** of the project.  
- **Workflows** ensure automation and reliability.  
- **Deployment** guarantees portability and scalability.  
- **CI/CD scripts** provide practical tools for execution and supervision.  

Together, they deliver a **complete technical infrastructure**, capable of supporting 
project evolution, passing audits, and enabling adoption by external partners.

##############################################