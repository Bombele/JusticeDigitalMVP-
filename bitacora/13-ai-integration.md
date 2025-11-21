# Bitácora 13 — Integración avanzada de IA conversacional

Este capítulo documenta la evolución hacia una **IA conversacional jurídica multilingüe**, conectada con la taxonomía de abusos y la arquitectura técnica de JusticeDigitalMVP.

---

## 🧠 Objetivo

- Transformar la API en un **asistente ciudadano multilingüe**.
- Ofrecer consultas jurídicas básicas en Español, Français, English, Swahili y Lingala.
- Detectar abusos institucionales en lenguaje natural y redirigir hacia `/reports`.
- Consolidar la narrativa ciudadana con la memoria activa del proyecto.

---

## ⚙️ Integración técnica

- **FastAPI** → nuevo endpoint `/consultation`.
- **Hugging Face Transformers** → modelo multilingüe `xlm-roberta-base` para clasificación de texto.
- **spaCy** → soporte NLP básico y filtrado.
- **SQLAlchemy + PostgreSQL** → persistencia de denuncias y estadísticas.
- **Taxonomía multilingüe (`abuse_types.py`)** → referencia estable para códigos internos.

---

## 🌍 Ejemplo multilingüe

### Español
```http
POST /consultation?lang=es
{
  "question": "El funcionario me pidió dinero para procesar mi caso"
}
