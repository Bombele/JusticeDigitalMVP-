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
