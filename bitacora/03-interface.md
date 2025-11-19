# 03 - Interfaz / Interface

## ES — Interfaz

La interfaz inicial de JusticeDigitalMVP es un formulario ciudadano simple que permite:

- Ingresar el texto de la denuncia.  
- Seleccionar el tipo de abuso (según la tipología documentada).  
- Enviar la información al backend (FastAPI).  

El backend procesa el texto, lo anonimiza con spaCy y guarda el reporte en la base de datos SQLite.  
La respuesta incluye el **ID del reporte** y el **texto anonimizado**, que puede ser consultado posteriormente.

Este diseño minimalista asegura accesibilidad y transparencia, y puede evolucionar hacia aplicaciones más completas (React, Streamlit, dashboards).

---

## FR — Interface

L’interface initiale de JusticeDigitalMVP est un formulaire citoyen simple qui permet :

- Saisir le texte de la dénonciation.  
- Sélectionner le type d’abus (selon la typologie documentée).  
- Envoyer l’information au backend (FastAPI).  

Le backend traite le texte, l’anonymise avec spaCy et enregistre le rapport dans la base de données SQLite.  
La réponse inclut l’**ID du rapport** et le **texte anonymisé**, consultables ultérieurement.

Ce design minimaliste garantit l’accessibilité et la transparence, et peut évoluer vers des applications plus complètes (React, Streamlit, tableaux de bord).

---

## Metadatos / Métadonnées

- Autor / Auteur : Bombele  
- Fecha / Date : 2025-11-19  
- Ruta / Chemin : bitacora/03-interface.md
