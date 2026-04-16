# PRD - Trabajo_final_v2

## Problema
`Trabajo_final` cumple la base funcional, pero mezcla menús, validaciones, lógica de negocio y persistencia en módulos planos. Eso dificulta entender el flujo, rastrear errores y probar manualmente los casos heredados.

## Objetivo
Crear una copia mejorada que conserve el funcionamiento observable del sistema actual, incluyendo errores y rarezas existentes cuando no bloqueen la migración, pero con mejor estructura, legibilidad y trazabilidad.

## Alcance
- Nueva carpeta `Trabajo_final_v2`.
- Arquitectura simple por capas estilo MVC.
- Persistencia concreta centralizada en JSON/TXT.
- Documentación técnica y guía de pruebas manuales.
- Pruebas automatizadas acotadas sobre piezas estables.

## Reglas conservadas
- Autenticación por rol admin/residente con claves hardcodeadas.
- Menús y flujo general de consola.
- Restricciones previas a herramientas, préstamos y reportes.
- Lógica observable actual de CRUD, préstamos y reportes.

## Impacto técnico
- Se elimina el acceso directo a archivos desde menús y scripts planos.
- Se concentra la escritura de historial en un servicio de trazabilidad.
- Se prepara el proyecto para que la persistencia pueda cambiar más adelante sin rehacer la navegación CLI.

## Riesgos
- Algunos comportamientos heredados son inconsistentes y se conservan a propósito.
- La equivalencia es de comportamiento general observable, no de replicar cada defecto byte a byte.
- La salida visual mejora, por lo que la comparación debe centrarse en flujos y resultados, no en texto idéntico.
