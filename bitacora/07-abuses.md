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
git add bitacora/07-abuses.md
git commit -m "Extend abuse taxonomy to 5 languages and link to API architecture"
abuse_types = {
    "es": {
        "procedural_delay": "Retrasos procesales",
        "medical_neglect": "Falta de atención médica",
        "extortion": "Extorsión de funcionarios",
        "abuse_of_power": "Abuso de poder",
        "judicial_discrimination": "Discriminación judicial",
        "administrative_corruption": "Corrupción administrativa",
        "obstruction_of_justice": "Obstrucción de justicia",
        "other_abuses": "Otros abusos"
    },
    "fr": {
        "procedural_delay": "Retards procéduraux",
        "medical_neglect": "Manque de soins médicaux",
        "extortion": "Extorsion par des fonctionnaires",
        "abuse_of_power": "Abus de pouvoir",
        "judicial_discrimination": "Discrimination judiciaire",
        "administrative_corruption": "Corruption administrative",
        "obstruction_of_justice": "Entrave à la justice",
        "other_abuses": "Autres abus"
    },
    "en": {
        "procedural_delay": "Procedural delays",
        "medical_neglect": "Lack of medical care",
        "extortion": "Extortion by officials",
        "abuse_of_power": "Abuse of power",
        "judicial_discrimination": "Judicial discrimination",
        "administrative_corruption": "Administrative corruption",
  # Tipología de abusos y arquitectura IA+informática

Se ha añadido el archivo [`bitacora/07-abuses.md`](bitacora/07-abuses.md) con la tipología multilingüe (ES, FR, EN, SW, LN) de abusos institucionales y la descripción de la alianza IA + informática.

---

## 🧩 Tipología multilingüe de abusos institucionales

| Código interno            | Español                    | Français                      | English                     | Swahili                          | Lingala                                |
|---------------------------|----------------------------|-------------------------------|-----------------------------|-----------------------------------|----------------------------------------|
| procedural_delay          | Retrasos procesales        | Retards procéduraux           | Procedural delays           | Muda ya mchakato                 | Nkɔkɔ ya procédure                     |
| medical_neglect           | Falta de atención médica   | Manque de soins médicaux      | Lack of medical care        | Kukosa huduma za afya            | Kozanga lisungi ya nzoto               |
| extortion                 | Extorsión de funcionarios  | Extorsion par des fonctionnaires | Extortion by officials    | Ufisadi wa maafisa               | Kosɛnga mbongo na bakonzi              |
| abuse_of_power            | Abuso de poder             | Abus de pouvoir               | Abuse of power              | Matumizi mabaya ya mamlaka        | Kosalelaka makasi na kobebisa          |
| judicial_discrimination   | Discriminación judicial    | Discrimination judiciaire     | Judicial discrimination     | Ubaguzi wa kimahakama            | Diskriminasyon ya bosambisi            |
| administrative_corruption | Corrupción administrativa  | Corruption administrative     | Administrative corruption   | Ufisadi wa kiutawala             | Kokɔrɔpɔ ya administration             |
| obstruction_of_justice    | Obstrucción de justicia    | Entrave à la justice          | Obstruction of justice      | Kuzuia haki                      | Kofunda bosambisi                      |
| other_abuses              | Otros abusos               | Autres abus                   | Other abuses                | Mengine ya unyanyasaji           | Bamosusu ya bokosi                     |

---

## 🧠 Integración técnica

Cada categoría tiene un **código interno** que se utiliza en la base de datos y en los endpoints de la API.  
Las respuestas y visualizaciones se adaptan automáticamente al idioma del usuario gracias al archivo `abuse_types.py`.

Ejemplo de uso en `/stats`:

```python
from abuse_types import abuse_types

label = abuse_types[lang].get(tipo_abuso, tipo_abuso)
