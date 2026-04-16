# Arquitectura de `Trabajo_final_v2`

## Objetivo
La nueva versión conserva el comportamiento observable de `Trabajo_final`, pero organiza la aplicación para que los flujos puedan rastrearse, probarse manualmente y evolucionar sin depender de módulos con responsabilidades mezcladas.

## Capas
- `views`: menús, mensajes de salida y renderizado de registros.
- `controllers`: navegación CLI y coordinación entre entrada de usuario y servicios.
- `services`: lógica actual del sistema, incluyendo validaciones, transformaciones, reportes, autenticación y préstamos.
- `models`: dataclasses simples para representar registros creados dentro del flujo.
- `persistence`: acceso centralizado a JSON/TXT mediante implementaciones concretas.

## Criterios de diseño
- No se usan interfaces abstractas.
- La persistencia actual sigue siendo archivos locales.
- La aplicación mantiene comportamientos heredados, incluso varios resultados defectuosos, para no alterar la referencia funcional.
- La trazabilidad mejora mediante mensajes más consistentes y registros con contexto `modulo.accion`.

## Evolución futura
Para migrar a base de datos u ORM, el punto de reemplazo es `persistence/`. Los servicios y controladores ya no acceden directamente a archivos ni a rutas hardcodeadas.
