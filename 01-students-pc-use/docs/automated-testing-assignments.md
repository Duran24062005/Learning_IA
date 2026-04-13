# Testeo Automatico - Modulo de Asignaciones

## Objetivo del modulo
Definir la estrategia de automatizacion para el modulo de asignaciones a partir de los casos manuales de [manual-testing-assignments.md](/home/alexi-dg/Desktop/GitHub_Repositories/IA/01-students-pc-use/docs/manual-testing-assignments.md), cubriendo reglas de elegibilidad, historial y devolucion de equipos.

## Estado actual de automatizacion
- Framework disponible: `pytest` en backend.
- Cobertura automatica existente:
  - asignacion valida a estudiante activo con computador disponible
  - rechazo por computador no disponible
  - rechazo por estudiante inactivo
  - devolucion que libera el computador
  - consulta de historial filtrado
- Archivo actual relacionado: [test_assignments.py](/home/alexi-dg/Desktop/GitHub_Repositories/IA/01-students-pc-use/backend/tests/test_assignments.py)
- No existe automatizacion frontend para formulario, selectores y tabla de historial.

## Comando de ejecucion actual
Desde `01-students-pc-use/backend`:

```bash
pytest
```

## Alcance automatico recomendado
- Prioridad 1: pruebas de servicio sobre reglas de negocio y transiciones de estado.
- Prioridad 2: pruebas de API sobre contratos para crear, listar y devolver asignaciones.
- Prioridad 3: pruebas de UI futuras para selectores filtrados, boton deshabilitado y tabla operativa.

## Trazabilidad manual -> automatica

| Caso manual | Cobertura automatica objetivo | Estado |
| --- | --- | --- |
| ASG-01 Asignacion valida | Test de servicio para create exitoso | Cubierto parcialmente |
| ASG-02 Solo estudiantes activos en selector | Test UI o de datos fuente del formulario | Pendiente |
| ASG-03 Solo computadores disponibles en selector | Test UI o de datos fuente del formulario | Pendiente |
| ASG-04 Bloqueo sin opciones | Test UI de boton deshabilitado | Pendiente |
| ASG-05 Cambio automatico a `assigned` | Test de servicio post-asignacion | Cubierto parcialmente |
| ASG-06 Historial y contadores | Test API/UI de listado y resumen | Pendiente |
| ASG-07 Devolucion exitosa | Test de servicio para `return_assignment` | Cubierto parcialmente |
| ASG-08 Liberacion automatica del computador | Test de servicio/API verificando `available` tras devolucion | Cubierto parcialmente |
| ASG-09 Rechazo a estudiante inactivo | Test de servicio ya existente y test API adicional | Parcialmente cubierto |
| ASG-10 Rechazo a computador no disponible | Test de servicio ya existente y test API adicional | Parcialmente cubierto |
| ASG-11 Rechazo de doble devolucion | Test de servicio/API sobre segunda devolucion | Pendiente |
| ASG-12 Ciclo completo asignar/devolver | Test integrado de servicio | Pendiente |

## Casos automaticos a implementar

### Suite de servicio
Archivo recomendado: `backend/tests/test_assignments.py`

- `test_assign_computer_to_active_student`
  - ya existe y debe conservarse
- `test_reject_assignment_when_computer_unavailable`
  - ya existe y debe conservarse
- `test_reject_assignment_to_inactive_student`
  - ya existe y debe conservarse
- `test_return_assignment_frees_computer`
  - ya existe y debe conservarse
- `test_assignment_history_filters`
  - ya existe y debe conservarse
- `test_reject_assignment_when_computer_already_has_active_assignment`
  - valida doble asignacion simultanea del mismo equipo
- `test_return_assignment_rejects_double_return`
  - valida rechazo de segunda devolucion
- `test_list_assignments_filters_active_only`
  - valida el filtro `active_only=True`
- `test_list_assignments_filters_by_computer_id`
  - valida filtro por computador
- `test_complete_assignment_cycle_keeps_consistent_history`
  - valida ciclo completo de asignar y devolver

### Suite de API
Archivo recomendado: `backend/tests/test_assignments_api.py`

- `test_post_assignments_returns_201`
- `test_post_assignments_rejects_inactive_student`
- `test_post_assignments_rejects_unavailable_computer`
- `test_post_assignments_rejects_unknown_student`
- `test_post_assignments_rejects_unknown_computer`
- `test_get_assignments_returns_history`
- `test_get_assignments_filters_active_only`
- `test_get_assignments_filters_by_student_id`
- `test_get_assignments_filters_by_computer_id`
- `test_post_assignment_return_closes_assignment`
- `test_post_assignment_return_rejects_double_return`
- `test_post_assignment_return_returns_404_for_unknown_assignment`

### Suite de UI futura
Archivo recomendado cuando exista runner frontend: `frontend/src/pages/AssignmentsPage.test.tsx`

- render del formulario y tabla de historial
- filtrado visual de estudiantes activos
- filtrado visual de computadores disponibles
- boton deshabilitado cuando falta alguna fuente valida de seleccion
- alta exitosa con refresco de datos de estudiantes y computadores
- devolucion con cambio de boton a `Cerrada`
- actualizacion de contadores `Historial` y `Activas`

## Datos y fixtures recomendados
- Reutilizar factories de estudiante y computador con overrides.
- Crear helper de asignacion para escenarios integrados.
- Dataset minimo recomendado:
  - 1 estudiante activo
  - 1 estudiante inactivo
  - 1 computador disponible
  - 1 computador en mantenimiento
  - 1 asignacion activa
  - 1 asignacion cerrada

## Criterio de aprobacion automatico del modulo
- Todas las reglas de negocio del flujo de asignacion y devolucion deben estar cubiertas a nivel servicio.
- Los contratos HTTP deben validarse a nivel API, en especial errores por conflicto y no encontrado.
- Los escenarios dependientes de selectores y botones pueden quedar como deuda controlada hasta que exista infraestructura de frontend, pero deben conservarse en esta especificacion para no perder trazabilidad.
