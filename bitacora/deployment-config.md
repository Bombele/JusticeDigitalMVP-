# 08 - Configuración de despliegue / Configuration de déploiement

## ES — Configuración de despliegue

Para garantizar que Railway instale correctamente las dependencias y ejecute la API FastAPI sin errores, se añadieron dos archivos clave:

### 1. `requirements.txt`
Contiene los paquetes esenciales del proyecto:
- `fastapi`, `uvicorn`, `sqlalchemy`, `spacy`  
- `pydantic`, `python-dotenv`

Este archivo permite que Railway instale automáticamente todo lo necesario para levantar el servicio.

### 2. `railway.json`
Define el comando de inicio para el entorno Railway:
```json
{
  "start": "uvicorn main:app --host 0.0.0.0 --port $PORT"
}
