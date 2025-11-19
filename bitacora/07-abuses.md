# 07 - Tipología de abusos / Typologie des abus

## Introducción / Introduction

**ES**  
Este documento agrupa la tipología de abusos que el proyecto recoge y documenta, y explica cómo la alianza entre IA y ciencias informáticas puede ayudar a identificar, anonimizar y analizar casos.

**FR**  
Ce document répertorie la typologie des abus recensés par le projet et décrit comment l’alliance IA + informatique permet d’identifier, d’anonymiser et d’analyser les cas.

---

## Tipos de abusos (ES)

1. Retrasos procesales — demoras injustificadas en juicios, audiencias o trámites.  
2. Falta de atención médica — negación o demora en servicios de salud básicos.  
3. Falta de atención integral — ausencia de acompañamiento social, psicológico o jurídico.  
4. Violaciones de derechos humanos — actos que vulneran garantías fundamentales.  
5. Extorsión por parte de funcionarios — exigencia de dinero o favores ilegales.  
6. Abogados pidiendo dinero con supuestos acuerdos — aprovechamiento de la desesperación con o sin complicidad institucional.  
7. Abuso de poder — decisiones arbitrarias o uso indebido de la autoridad.  
8. Fiscales imputando delitos que no corresponden — acusaciones falsas o desproporcionadas.  
9. Discriminación judicial — trato desigual por origen, género, condición social o migratoria.  
10. Corrupción administrativa — manipulación de expedientes, cobros indebidos, favoritismos.  
11. Obstrucción de justicia — ocultamiento de pruebas, manipulación de testigos, presión indebida.  
12. Otros abusos — campo libre para descripciones no contempladas arriba.

---

## Types d'abus (FR)

1. Retards procéduraux — délais injustifiés dans les procès, audiences ou procédures.  
2. Manque de soins médicaux — refus ou retard dans l’accès aux services de santé.  
3. Absence d’accompagnement global — manque d’appui social, psychologique ou juridique.  
4. Violations des droits humains — actes portant atteinte aux garanties fondamentales.  
5. Extorsion par des fonctionnaires — exiger de l’argent ou des faveurs illégales.  
6. Avocats réclamant de l’argent sous prétexte d’accords — exploitation de la détresse des justiciables.  
7. Abus de pouvoir — décisions arbitraires ou usage inapproprié de l’autorité.  
8. Procureurs imputant des délits non fondés — accusations fausses ou disproportionnées.  
9. Discrimination judiciaire — traitement inégal selon origine, genre, statut social ou migratoire.  
10. Corruption administrative — manipulation de dossiers, paiements indus, favoritisme.  
11. Entrave à la justice — dissimulation de preuves, manipulation de témoins, pressions.  
12. Autres abus — champ libre pour des cas non listés ci‑dessus.

---

## Alianza IA + Informática / Alliance IA + Informatique

**ES**  
Componentes clave:
- spaCy (NLP) para reconocimiento de entidades y anonimización automática.  
- FastAPI + Pydantic para endpoints robustos y validación.  
- SQLAlchemy + SQLite (prototipo) → PostgreSQL (producción).  
- Frontend simple (HTML/React/Streamlit).  
- Seguridad: `.env`, cifrado en reposo, autenticación JWT.  
- Analytics: clustering, patrones, reportes exportables.

**FR**  
Composants clés :
- spaCy (NLP) pour la reconnaissance d’entités et l’anonymisation automatique.  
- FastAPI + Pydantic pour des endpoints robustes et la validation.  
- SQLAlchemy + SQLite (prototype) → PostgreSQL (production).  
- Frontend simple (HTML/React/Streamlit).  
- Sécurité : `.env`, chiffrement au repos, authentification JWT.  
- Analytics : clustering, détection de patterns, rapports exportables.

---

## Recomendaciones / Recommandations

**ES**  
- Añadir clasificación automática de abusos.  
- Implementar análisis de sentimiento y urgencia.  
- Desarrollar dashboard para visualización agregada.  
- Migrar a PostgreSQL y reforzar seguridad.  

**FR**  
- Ajouter classification automatique des abus.  
- Implémenter analyse des sentiments et urgence.  
- Développer un tableau de bord pour visualisation agrégée.  
- Migrer vers PostgreSQL et renforcer la sécurité.

---

## Metadatos / Métadonnées

- Autor / Auteur : Bombele  
- Fecha / Date : 2025-11-19  
- Ruta / Chemin : bitacora/07-abuses.md
