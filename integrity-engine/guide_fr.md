##############################################
# 📖 Guide détaillé – Integrity Engine
##############################################

## 1. Objectif
Le module **Integrity Engine** assure la traçabilité et la robustesse institutionnelle :
- Journaux append-only pour garantir l’intégrité des écritures.
- Arbres de Merkle pour valider la cohérence des données.
- Signatures institutionnelles pour authentifier les opérations.
- Export CSV/PDF pour audit externe.

----------------------------------------------

## 2. Dossier `src/`
Ce dossier contient le code source du moteur d’intégrité.

📂 integrity-engine/src/
- log_append.py         → Ajout dans le journal append-only.
- merkle_tree.py        → Génération et validation d’arbres de Merkle.
- signature.py          → Gestion des signatures institutionnelles.
- integrity_export.py   → Export des journaux pour audit (CSV/PDF).

👉 **Bonne pratique** :
- Chaque fichier doit inclure une fonction principale + une fonction de log.
- Documenter les algorithmes (Merkle, signatures) dans le code et dans `docs/`.

----------------------------------------------

## 3. Dossier `tests/`
Ce dossier contient les tests unitaires et fonctionnels.

📂 integrity-engine/tests/
- test_log_append.py        → Vérifie l’ajout dans le journal.
- test_merkle_tree.py       → Vérifie la cohérence du Merkle tree.
- test_signature.py         → Vérifie la signature institutionnelle.
- test_integrity_export.py  → Vérifie l’export CSV/PDF.

👉 **Bonne pratique** :
- Utiliser `pytest` avec des cas simples au début (`assert True`).
- Ajouter ensuite des cas de corruption simulée pour tester la robustesse.

----------------------------------------------

## 4. Dossier `docs/`
Ce dossier contient la documentation institutionnelle et technique.

📂 integrity-engine/docs/
- bitacoras/integrity.md    → Journal trilingue (FR/ES/EN) du module intégrité.
- guides/integrity_usage.md → Guide pratique d’utilisation du moteur d’intégrité.

👉 **Bonne pratique** :
- La bitácora doit être mise à jour à chaque commit ou évolution.
- Le guide doit expliquer comment utiliser le moteur pour audit et conformité.

----------------------------------------------

## 5. Dossier `infra/`
Ce dossier contient l’infrastructure technique pour CI/CD et déploiement.

📂 integrity-engine/infra/
- ci-cd/integrity-ci.yml    → Workflow CI/CD spécifique au module intégrité.
- scripts/lint_integrity.sh → Linting du code.
- scripts/coverage_integrity.sh → Couverture des tests.
- scripts/deploy_integrity.sh   → Déploiement du moteur d’intégrité.

👉 **Bonne pratique** :
- Automatiser lint + tests à chaque commit.
- Déployer uniquement après validation des tests et export.

----------------------------------------------

## 6. Workflow de développement
1. Créer la branche `feature/integrity-engine`.
2. Ajouter fichiers vides + README trilingue.
3. Écrire tests placeholders (`assert True`).
4. Remplir progressivement `src/` avec les fonctions.
5. Mettre à jour `docs/bitacoras/integrity.md` à chaque étape.
6. Activer CI/CD (lint + tests automatiques).
7. Fusionner dans `develop`, puis dans `main`.

----------------------------------------------

## 7. Résultat attendu
- `src/` → Code robuste et auditable.
- `tests/` → Vérifications unitaires et fonctionnelles.
- `docs/` → Traçabilité documentaire et guides pratiques.
- `infra/` → Automatisation CI/CD et déploiement.  
Ensemble → un **moteur d’intégrité complet**, prêt pour audit et certification.

----------------------------------------------

## 8. Conclusion / Synthèse
Le module **Integrity Engine** est le **garant institutionnel de la traçabilité**.  
- Le code (`src/`) implémente journaux, Merkle trees et signatures.  
- Les tests (`tests/`) valident la robustesse face aux corruptions.  
- La documentation (`docs/`) assure transparence et auditabilité.  
- L’infrastructure (`infra/`) automatise la qualité et le déploiement.  

Ensemble, ils offrent une **ossature technique et institutionnelle solide**, 
capable de résister aux audits, de renforcer la crédibilité et de préparer 
l’adoption par des partenaires externes.

##############################################
