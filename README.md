## Tipos de abusos / Types d’abus

La plataforma documenta y anonimiza diferentes formas de abusos institucionales.  
Consulta el detalle completo en [`bitacora/07-abuses.md`](bitacora/07-abuses.md).

### Ejemplos principales:
- Retrasos procesales / Retards procéduraux  
- Falta de atención médica / Manque de soins médicaux  
- Extorsión por parte de funcionarios / Extorsion par des fonctionnaires  
- Abuso de poder / Abus de pouvoir  
- Discriminación judicial / Discrimination judiciaire  
- Corrupción administrativa / Corruption administrative  
- Obstrucción de justicia / Entrave à la justice  
- Otros abusos / Autres abus
## 📊 Reportes y estadísticas

La plataforma ahora incluye endpoints para consultar y exportar estadísticas de las denuncias:

### 1. `/stats`
Devuelve un JSON con:
- Total de denuncias registradas
- Conteo por tipo de abuso

**Ejemplo de respuesta:**
```json
{
  "total_denuncias": 12,
  "por_tipo": {
    "corrupcion": 5,
    "abuso_de_poder": 3,
    "discriminacion": 4
  }
}
## 🌍 Multilingue

La plateforme JusticeDigitalMVP est disponible en **5 langues** :

- 🇪🇸 Español  
- 🇫🇷 Français  
- 🇬🇧 English  
- 🇹🇿 Swahili  
- 🇨🇩 Lingala  

### Comment utiliser

Chaque endpoint accepte un paramètre `lang` :

- `GET /?lang=fr` → Bienvenue sur JusticeDigitalMVP  
- `GET /?lang=en` → Welcome to JusticeDigitalMVP  
- `GET /?lang=sw` → Karibu JusticeDigitalMVP  
- `GET /?lang=ln` → Boyei malamu na JusticeDigitalMVP  
- `GET /?lang=es` → Bienvenido a JusticeDigitalMVP  

### Exemple de création de dénonciation

```json
POST /reports?lang=sw
{
  "texto": "Jaji John alitumia vibaya mamlaka yake",
  "tipo_abuso": "abuse_of_power",
  "idioma": "sw"
}
