# 09 - Reportes y estadísticas / Rapports et statistiques

## ES — Reportes y estadísticas

Se añadieron dos endpoints clave al servicio FastAPI:

- **`/stats`** → Devuelve un JSON con:
  - Total de denuncias registradas
  - Conteo por tipo de abuso

- **`/stats/export`** → Permite descargar las estadísticas en formato CSV, con columnas:
  - Tipo de abuso
  - Cantidad de denuncias

### Impacto
Este módulo convierte la base de datos en evidencia estructurada, facilita la transparencia ciudadana y abre la posibilidad de análisis externo y visualización en dashboards.

---

## FR — Rapports et statistiques

Deux endpoints essentiels ont été ajoutés au service FastAPI :

- **`/stats`** → Retourne un JSON avec :
  - Nombre total de dénonciations enregistrées
  - Comptage par type d’abus

- **`/stats/export`** → Permet de télécharger les statistiques au format CSV, avec colonnes :
  - Type d’abus
  - Nombre de dénonciations

### Impact
Ce module transforme la base de données en mémoire structurée, facilite la transparence citoyenne et ouvre la voie à l’analyse externe et aux visualisations.

---

## Metadatos / Métadonnées

- Autor / Auteur : Bombele  
- Fecha / Date : 2025-11-21  
- Ruta / Chemin : bitacora/09-reports.md
