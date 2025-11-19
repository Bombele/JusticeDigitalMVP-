# 02 - Anonimización / Anonymisation

## ES — Anonimización

La anonimización es el núcleo de JusticeDigitalMVP.  
Se utiliza **spaCy** (modelo español `es_core_news_sm`) para detectar entidades sensibles como:

- PERSON (nombres propios)  
- ORG (instituciones, empresas)  
- LOC (lugares, ciudades, países)  
- DATE (fechas)  
- Otros tipos relevantes

El sistema reemplaza automáticamente estas entidades por etiquetas genéricas (`[PERSON]`, `[ORG]`, etc.), protegiendo la identidad de los denunciantes y permitiendo que los reportes puedan ser publicados sin riesgo.

La anonimización garantiza que los datos puedan ser compartidos y analizados sin comprometer la seguridad de las personas involucradas.

---

## FR — Anonymisation

L’anonymisation est au cœur de JusticeDigitalMVP.  
On utilise **spaCy** (modèle espagnol `es_core_news_sm`) pour détecter les entités sensibles telles que :

- PERSON (noms propres)  
- ORG (institutions, entreprises)  
- LOC (lieux, villes, pays)  
- DATE (dates)  
- Autres types pertinents

Le système remplace automatiquement ces entités par des étiquettes génériques (`[PERSON]`, `[ORG]`, etc.), protégeant l’identité des plaignants et permettant la publication des rapports sans risque.

L’anonymisation garantit que les données peuvent être partagées et analysées sans compromettre la sécurité des personnes concernées.

---

## Metadatos / Métadonnées

- Autor / Auteur : Bombele  
- Fecha / Date : 2025-11-19  
- Ruta / Chemin : bitacora/02-anonymisation.md
