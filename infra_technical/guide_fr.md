##############################################
# 📖 Guide détaillé – infra_technical/
##############################################

## 1. Objectif
Le dossier `infra_technical/` regroupe toutes les composantes techniques nécessaires 
pour automatiser, déployer et superviser le projet.  
Il constitue la **colonne vertébrale technique** qui complète la documentation institutionnelle.

----------------------------------------------

## 2. Dossier `infra_technical/workflows`
Ce dossier contient les workflows d’intégration et de livraison continue.

📂 infra_technical/workflows/
- ci.yml              → Workflow CI (lint, tests, couverture).
- cd.yml              → Workflow CD (déploiement automatisé).
- monitor.yml         → Workflow de monitoring et alertes.
- rollback.yml        → Procédure de rollback en cas d’échec.

👉 **Bonne pratique** :
- Définir des jobs séparés (lint, test, build, deploy).
- Utiliser des secrets sécurisés pour credentials.
- Ajouter des notifications (Slack, email) en cas d’échec.

----------------------------------------------

## 3. Dossier `infra_technical/deployment`
Ce dossier contient les configurations de déploiement.

📂 infra_technical/deployment/
- docker-compose.yml  → Déploiement local avec Docker.
- k8s-deployment.yaml → Déploiement Kubernetes (pods, services).
- monitoring-config.yml → Configurations Prometheus/Grafana.
- env.example         → Exemple de variables d’environnement.

👉 **Bonne pratique** :
- Séparer environnements (dev, staging, prod).
- Documenter chaque paramètre dans `env.example`.
- Vérifier la compatibilité avec CI/CD avant mise en production.

----------------------------------------------

## 4. Dossier `infra_technical/ci-cd`
Ce dossier contient les scripts et outils pour CI/CD.

📂 infra_technical/ci-cd/
- lint.sh             → Vérifie la qualité du code.
- coverage.sh         → Mesure la couverture des tests.
- deploy.sh           → Script de déploiement automatisé.
- monitor.sh          → Vérifie l’état des services déployés.
- cleanup.sh          → Nettoyage des ressources après rollback.

👉 **Bonne pratique** :
- Scripts modulaires et réutilisables.
- Inclure logs et codes de retour clairs.
- Tester chaque script indépendamment avant intégration dans workflows.

----------------------------------------------

## 5. Workflow technique global
1. **Développement** : commit sur branche feature → déclenche CI (lint + tests).
2. **Intégration** : merge dans `develop` → déclenche build + couverture.
3. **Déploiement** : merge dans `main` → déclenche CD (Docker/K8s).
4. **Monitoring** : workflows + scripts surveillent disponibilité et alertes.
5. **Rollback** : en cas d’échec, exécution automatique de `rollback.yml` + `cleanup.sh`.

----------------------------------------------

## 6. Résultat attendu
- `workflows` → Automatisation CI/CD et monitoring.
- `deployment` → Configurations Docker/Kubernetes.
- `ci-cd` → Scripts techniques modulaires.  
Ensemble → un **système technique robuste**, auditable et prêt pour production.

----------------------------------------------

## 7. Conclusion / Synthèse
Le dossier `infra_technical/` est la **colonne vertébrale opérationnelle** du projet.  
- Les **workflows** assurent l’automatisation et la fiabilité.  
- Le **deployment** garantit la portabilité et la scalabilité.  
- Le **ci-cd** fournit les outils pratiques pour exécuter et superviser.  

Ensemble, ils offrent une **infrastructure technique complète**, capable de soutenir 
l’évolution du projet, de résister aux audits et de faciliter l’adoption par des partenaires externes.

##############################################
