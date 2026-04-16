# Manual Testing Guide

## Ejecución
- Original: `python3 Code-Optimization/Trabajo_final/main.py`
- Refactor: `cd Code-Optimization/Trabajo_final_v2 && python3 main.py`

## Credenciales
- Admin: `admin123`
- Residente: `residente123`

## Flujos a comparar
- Login admin y login residente.
- Restricción de gestión de herramientas sin categorías.
- Restricción de préstamos sin usuarios/herramientas.
- CRUD de categorías.
- CRUD de usuarios.
- CRUD de herramientas.
- Solicitud de préstamo por residente.
- Gestión de préstamo por admin.
- Reportes de stock, estado, historial y uso.

## Qué validar
- Que el recorrido general siga siendo equivalente al original.
- Que los mensajes de seguimiento indiquen mejor qué módulo y acción se ejecutó.
- Que los logs en `Trabajo_final_v2/data/historial.txt` muestren contexto útil para rastreo manual.
- Que comportamientos heredados sigan siendo observables cuando aparezcan.

## Casos útiles
- Crear categorías antes de crear herramientas.
- Crear usuarios y herramientas antes de probar préstamos.
- Pedir más unidades que las disponibles para observar rechazo por stock.
- Ejecutar reportes con y sin datos para revisar mensajes y trazas.
