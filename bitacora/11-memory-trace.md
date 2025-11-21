# 11 - Memoria activa y trazabilidad / Mémoire active et traçabilité

## ES — Memoria activa

Se añadió el endpoint **`/timeline`** que devuelve los hitos del proyecto:

- Despliegues técnicos (Railway, Replit, GitHub)  
- Mejoras funcionales (anonimización, estadísticas, exportación CSV)  
- Denuncias emblemáticas registradas en la base de datos  

### Ejemplo de respuesta

```json
{
  "timeline": [
    {"fecha": "2025-11-18", "evento": "Inicio del proyecto JusticeDigitalMVP"},
    {"fecha": "2025-11-19", "evento": "Primer endpoint de anonimización (/anonymize)"},
    {"fecha": "2025-11-20", "evento": "Integración de estadísticas (/stats) y exportación CSV"},
    {"fecha": "2025-11-21", "evento": "Diagnóstico de crash en Railway y resiliencia en GitHub"},
    {"fecha": "2025-11-21", "evento": "Denuncia #12 registrada: abuso_de_poder"}
  ]
}
