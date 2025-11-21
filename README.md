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
## 🌍 Taxonomie multilingue des abus institutionnels

La plateforme JusticeDigitalMVP utilise une **taxonomie multilingue** pour classifier les abus institutionnels.  
Chaque catégorie possède un **code interne** stable (utilisé dans la base de données et les endpoints), et une traduction disponible en **Español, Français, English, Swahili, Lingala**.

### Catégories disponibles

| Code interne             | Español                    | Français                      | English                     | Swahili                          | Lingala                                |
|--------------------------|----------------------------|-------------------------------|-----------------------------|-----------------------------------|----------------------------------------|
| procedural_delay         | Retrasos procesales        | Retards procéduraux           | Procedural delays           | Muda ya mchakato                 | Nkɔkɔ ya procédure                     |
| medical_neglect          | Falta de atención médica   | Manque de soins médicaux      | Lack of medical care        | Kukosa huduma za afya            | Kozanga lisungi ya nzoto               |
| extortion                | Extorsión de funcionarios  | Extorsion par des fonctionnaires | Extortion by officials    | Ufisadi wa maafisa               | Kosɛnga mbongo na bakonzi              |
| abuse_of_power           | Abuso de poder             | Abus de pouvoir               | Abuse of power              | Matumizi mabaya ya mamlaka        | Kosalelaka makasi na kobebisa          |
| judicial_discrimination  | Discriminación judicial    | Discrimination judiciaire     | Judicial discrimination     | Ubaguzi wa kimahakama            | Diskriminasyon ya bosambisi            |
| administrative_corruption| Corrupción administrativa  | Corruption administrative     | Administrative corruption   | Ufisadi wa kiutawala             | Kokɔrɔpɔ ya administration             |
| obstruction_of_justice   | Obstrucción de justicia    | Entrave à la justice          | Obstruction of justice      | Kuzuia haki                      | Kofunda bosambisi                      |
| other_abuses             | Otros abusos               | Autres abus                   | Other abuses                | Mengine ya unyanyasaji           | Bamosusu ya bokosi                     |

---

### Exemple d’utilisation dans l’API

- **Endpoint `/stats`**  
  Retourne les statistiques avec les catégories traduites selon la langue choisie :

```json
GET /stats?lang=fr
{
  "message": "Statistiques",
  "total": 42,
  "por_tipo": {
    "Abus de pouvoir": 12,
    "Corruption administrative": 8,
    "Discrimination judiciaire": 5
  }
}
## 📝 Utilisation des codes internes dans `POST /reports`

Chaque abus institutionnel est identifié par un **code interne** stable (ex. `abuse_of_power`, `corruption`).  
Ces codes doivent être utilisés dans le champ `tipo_abuso` lors de la création d’une dénonciation.  
La réponse de l’API s’adapte automatiquement à la langue choisie (`?lang=fr`, `?lang=en`, etc.).

### Exemple en français

```http
POST /reports?lang=fr
Content-Type: application/json

{
  "texto": "Le juge a retardé le procès sans justification",
  "tipo_abuso": "procedural_delay",
  "idioma": "fr"
}
GET /stats?lang=fr
# JusticeDigitalMVP

Plataforma ciudadana para documentar abusos institucionales y fortalecer la justicia digital transcontinental.  
Construida con **FastAPI, spaCy, SQLAlchemy, Hugging Face Transformers, SQLite/PostgreSQL**.

---

## 🚀 Endpoints principales

- **`/reports`** → Crear denuncias con código interno de abuso.
- **`/stats`** → Estadísticas multilingües de abusos.
- **`/abuse-types`** → Lista de categorías disponibles en la lengua del usuario.
- **`/consultation`** → IA conversacional para orientación jurídica ciudadana.

---

## 🌍 Taxonomía multilingüe de abusos

Cada categoría tiene un **código interno** estable y traducciones en **Español, Français, English, Swahili, Lingala**.  
Ejemplo: `abuse_of_power` → "Abus de pouvoir" (fr), "Abuso de poder" (es), "Abuse of power" (en).

👉 Ver detalle en [`bitacora/07-abuses.md`](bitacora/07-abuses.md).

---

## 🧠 IA Conversacional

La plataforma integra **Hugging Face Transformers (xlm-roberta-base)** para análisis multilingüe.  
El endpoint `/consultation` permite:

- Reconocer abusos mencionados en lenguaje natural.
- Sugerir el código interno correspondiente.
- Redirigir al endpoint `/reports`.

Ejemplo:

```http
POST /consultation?lang=fr
{
  "user": "Camille",
  "question": "Le juge a retardé mon procès sans raison"
}
