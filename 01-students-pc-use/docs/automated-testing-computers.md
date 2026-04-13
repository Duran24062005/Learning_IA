# Testeo Automatico - Modulo de Computadores

## Objetivo del modulo
Definir la estrategia de automatizacion para el modulo de computadores tomando como base los casos manuales de [manual-testing-computers.md](/home/alexi-dg/Desktop/GitHub_Repositories/IA/01-students-pc-use/docs/manual-testing-computers.md), con foco en inventario, estados operativos y restricciones de negocio.

## Estado actual de automatizacion
- Framework disponible: `pytest` sobre backend.
- Cobertura automatica existente:
  - creacion de computador
  - rechazo de serial duplicado
- Archivo actual relacionado: [test_computers.py](/home/alexi-dg/Desktop/GitHub_Repositories/IA/01-students-pc-use/backend/tests/test_computers.py)
- No existe runner de pruebas de frontend para automatizar tabla, badges o acciones de UI.

## Comando de ejecucion actual
Desde `01-students-pc-use/backend`:

```bash
pytest
```

## Alcance automatico recomendado
- Prioridad 1: automatizar reglas de servicio sobre seriales y estados.
- Prioridad 2: automatizar contratos de API para creacion, listado y actualizacion.
- Prioridad 3: automatizar UI cuando exista infraestructura dedicada en frontend.

## Trazabilidad manual -> automatica

| Caso manual | Cobertura automatica objetivo | Estado |
| --- | --- | --- |
| COM-01 Registro disponible | Test de servicio para alta con estado `available` | Cubierto parcialmente |
| COM-02 Registro en mantenimiento | Test de servicio para alta con estado `maintenance` | Pendiente |
| COM-03 Campos requeridos | Test de API con `422` por payload incompleto | Pendiente |
| COM-04 Serial duplicado | Test de servicio/API por conflicto de serial | Parcialmente cubierto |
| COM-05 Tabla y contador | Test UI de renderizado y conteo | Pendiente |
| COM-06 Cambio a mantenimiento | Test de servicio/API para `PATCH status=maintenance` | Pendiente |
| COM-07 Cambio a disponible | Test de servicio/API para `PATCH status=available` | Pendiente |
| COM-08 Restriccion de estados validos | Test de servicio rechazando `assigned` manual | Pendiente |
| COM-09 Persistencia tras recarga | Test API de lectura posterior al update o test UI | Pendiente |
| COM-10 Regresion de altas y cambios | Suite integrada de varios cambios de estado | Pendiente |
| COM-11 Restriccion sobre equipo asignado | Test de servicio/API rechazando cambio manual con asignacion activa | Pendiente |

## Casos automaticos a implementar

### Suite de servicio
Archivo recomendado: `backend/tests/test_computers.py`

- `test_create_available_computer`
  - ya existe y puede renombrarse si se quiere mayor claridad
- `test_create_maintenance_computer`
  - valida alta con estado `maintenance`
- `test_reject_duplicate_serial`
  - ya existe y debe conservarse
- `test_reject_manual_create_with_assigned_status`
  - valida que `assigned` no pueda enviarse en creacion
- `test_update_computer_to_maintenance`
  - valida cambio manual de disponible a mantenimiento
- `test_update_computer_to_available`
  - valida cambio manual de mantenimiento a disponible
- `test_reject_update_computer_to_assigned_status`
  - valida rechazo de `assigned` en actualizacion manual
- `test_reject_manual_status_change_when_assignment_is_active`
  - valida restriccion sobre un equipo con asignacion activa
- `test_list_computers_returns_all_by_default`
  - valida listado general
- `test_list_computers_filters_available_only`
  - valida filtro `available_only=True`

### Suite de API
Archivo recomendado: `backend/tests/test_computers_api.py`

- `test_post_computers_returns_201`
- `test_post_computers_rejects_missing_required_fields`
- `test_post_computers_rejects_duplicate_serial`
- `test_post_computers_rejects_assigned_status`
- `test_get_computers_returns_inventory`
- `test_get_computers_filters_available_only`
- `test_patch_computers_updates_status`
- `test_patch_computers_rejects_assigned_status`
- `test_patch_computers_rejects_status_change_with_active_assignment`
- `test_patch_computers_returns_404_for_unknown_computer`

### Suite de UI futura
Archivo recomendado cuando exista runner frontend: `frontend/src/pages/ComputersPage.test.tsx`

- render de inventario y badge de estado
- actualizacion de contador `Disponibles`
- disparo de acciones `Marcar disponible` y `Mantenimiento`
- deshabilitacion de botones cuando el equipo esta `assigned`
- visualizacion de errores provenientes de API

## Datos y fixtures recomendados
- Factory reutilizable de computador con overrides para `serial_number` y `status`.
- Fixture integrada para computador con asignacion activa, reutilizable con el modulo de asignaciones.

## Criterio de aprobacion automatico del modulo
- Las reglas sobre serial unico y estados permitidos deben quedar cubiertas por pruebas de servicio.
- Las validaciones de entrada y salida deben quedar cubiertas por pruebas de API.
- La restriccion de no cambiar manualmente un equipo con asignacion activa debe quedar automatizada antes de considerar estable el modulo.
