# 05 - Estructura de datos / Structure des données

## ES — Estructura de datos

El modelo de datos de JusticeDigitalMVP se centra en la entidad **Denuncia**, que permite almacenar y consultar reportes ciudadanos.  
Los campos principales son:

- **id**: identificador único del reporte.  
- **original_text**: texto original de la denuncia (almacenado para referencia interna).  
- **anonymized_text**: versión anonimizada del texto, con entidades sensibles reemplazadas por etiquetas genéricas.  
- **tipo_abuso**: categoría del abuso según la tipología documentada.  

La persistencia se implementa inicialmente con **SQLite** para prototipos locales, y se proyecta migrar a **PostgreSQL** en entornos productivos.  
Se utiliza **SQLAlchemy** para definir el modelo y gestionar las operaciones de base de datos.

---

## FR — Structure des données

Le modèle de données de JusticeDigitalMVP est centré sur l’entité **Denuncia**, qui permet de stocker et de consulter les rapports citoyens.  
Les champs principaux sont :

- **id** : identifiant unique du rapport.  
- **original_text** : texte original de la dénonciation (stocké pour référence interne).  
- **anonymized_text** : version anonymisée du texte, avec les entités sensibles remplacées par des étiquettes génériques.  
- **tipo_abuso** : catégorie de l’abus selon la typologie documentée.  

La persistance est implémentée initialement avec **SQLite** pour les prototypes locaux, et une migration vers **PostgreSQL** est prévue pour les environnements de production.  
On utilise **SQLAlchemy** pour définir le modèle et gérer les opérations de base de données.

---

## Metadatos / Métadonnées

- Autor / Auteur : Bombele  
- Fecha / Date : 2025-11-19  
- Ruta / Chemin : bitacora/05-data.md
