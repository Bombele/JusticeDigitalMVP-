##############################################
# 📖 Guide détaillé – Dossiers institutionnels
##############################################

## 1. Objectif
Les dossiers `docs/guides` et `docs/bitacora` servent à :
- Garantir la traçabilité documentaire (bitácoras).
- Fournir des guides pratiques pour l’usage, le déploiement et l’audit.
- Donner une crédibilité institutionnelle au projet dès ses premières étapes.

----------------------------------------------

## 2. Dossier `docs/guides`
Ce dossier contient des **documents pratiques** pour les utilisateurs, partenaires et auditeurs.

📂 docs/guides/
- deployment.md   → Guide de déploiement (Docker, Kubernetes, CI/CD).
- compliance.md   → Normes de conformité (KYC/KYB, sanctions, certification).
- audit.md        → Procédures d’audit et checklist institutionnelle.
- cache_usage.md  → Guide spécifique au module cache.
- integrity_usage.md → Guide spécifique au module intégrité.
- sync_usage.md   → Guide spécifique au module synchro.
- security_usage.md → Guide spécifique au module sécurité.
- observability_usage.md → Guide spécifique au module observabilité.

👉 **Bonne pratique** : chaque guide doit être trilingue (FR/ES/EN) et contenir :
- Objectif du module ou procédure.
- Étapes pratiques.
- Notes institutionnelles (audit, conformité).
- Exemple minimal (code ou workflow).

----------------------------------------------

## 3. Dossier `docs/bitacora`
Ce dossier contient les **journaux trilingues** (bitácoras) pour chaque module.

📂 docs/bitacora/
- cache.md        → Journal du module cache.
- integrity.md    → Journal du module intégrité.
- sync.md         → Journal du module synchro.
- security.md     → Journal du module sécurité.
- observability.md → Journal du module observabilité.

👉 **Bonne pratique** : chaque bitácora doit suivre le format :
