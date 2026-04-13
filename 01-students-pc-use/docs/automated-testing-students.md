# Testeo Automatico - Modulo de Estudiantes

## Objetivo del modulo
Definir la estrategia de automatizacion para el modulo de estudiantes a partir de los casos manuales documentados en [manual-testing-students.md](/home/alexi-dg/Desktop/GitHub_Repositories/IA/01-students-pc-use/docs/manual-testing-students.md), manteniendo trazabilidad entre validaciones funcionales, reglas de negocio y cobertura automatica real del repositorio.

## Estado actual de automatizacion
- Framework disponible: `pytest` en `backend/tests/`.
- Infraestructura actual: base de datos `SQLite` en memoria definida en [conftest.py](/home/alexi-dg/Desktop/GitHub_Repositories/IA/01-students-pc-use/backend/tests/conftest.py).
- Cobertura automatica existente:
  - creacion de estudiante
  - rechazo de correo duplicado
- Archivo actual relacionado: [test_students.py](/home/alexi-dg/Desktop/GitHub_Repositories/IA/01-students-pc-use/backend/tests/test_students.py)
- No existe infraestructura de automatizacion para frontend en `frontend/package.json`.

## Comando de ejecucion actual
Desde `01-students-pc-use/backend`:

```bash
pytest
```

## Alcance automatico recomendado
- Prioridad 1: pruebas de servicio/backend sobre reglas de negocio y unicidad.
- Prioridad 2: pruebas de API sobre contratos HTTP para `POST /api/v1/students`, `GET /api/v1/students` y `PATCH /api/v1/students/{student_id}`.
- Prioridad 3: pruebas UI cuando exista infraestructura de frontend, para validar formulario, tabla y contadores.

## Trazabilidad manual -> automatica

| Caso manual | Cobertura automatica objetivo | Estado |
| --- | --- | --- |
| STU-01 Registro exitoso activo | Test de servicio para `create` con `is_active=True` | Parcialmente cubierto |
| STU-02 Registro exitoso inactivo | Test de servicio para `create` con `is_active=False` | Pendiente |
| STU-03 Campos requeridos | Test de API validando `422` por payload incompleto | Pendiente |
| STU-04 Formato de correo | Test de API validando rechazo de email invalido | Pendiente |
| STU-05 Documento duplicado | Test de servicio/API por conflicto de `document_id` | Pendiente |
| STU-06 Correo duplicado | Test de servicio por conflicto de `email` | Cubierto parcialmente |
| STU-07 Tabla y contadores | Test UI de renderizado y conteo | Pendiente |
| STU-08 Desactivar estudiante | Test de servicio/API para `PATCH is_active=False` | Pendiente |
| STU-09 Activar estudiante | Test de servicio/API para `PATCH is_active=True` | Pendiente |
| STU-10 Persistencia tras recarga | Test API de lectura posterior al update o test UI con refetch | Pendiente |
| STU-11 Regresion ligera | Suite agregada con multiples cambios de estado | Pendiente |

## Casos automaticos a implementar

### Suite de servicio
Archivo recomendado: `backend/tests/test_students.py`

- `test_create_active_student`
  - valida alta correcta con `is_active=True`
- `test_create_inactive_student`
  - valida alta correcta con `is_active=False`
- `test_reject_duplicate_student_document_id`
  - valida conflicto por `document_id` duplicado
- `test_reject_duplicate_student_email`
  - ya existe y debe conservarse
- `test_update_student_to_inactive`
  - valida cambio de estado a inactivo
- `test_update_student_to_active`
  - valida cambio de estado a activo
- `test_update_student_rejects_duplicate_document_id`
  - valida conflicto al editar documento hacia uno ya usado
- `test_update_student_rejects_duplicate_email`
  - valida conflicto al editar correo hacia uno ya usado
- `test_list_students_returns_all_by_default`
  - valida listado general
- `test_list_students_filters_active_only`
  - valida filtro `active_only=True`

### Suite de API
Archivo recomendado: `backend/tests/test_students_api.py`

- `test_post_students_returns_201`
- `test_post_students_rejects_missing_required_fields`
- `test_post_students_rejects_invalid_email`
- `test_post_students_rejects_duplicate_document_id`
- `test_post_students_rejects_duplicate_email`
- `test_get_students_returns_registered_students`
- `test_get_students_filters_active_only`
- `test_patch_students_updates_activation_state`
- `test_patch_students_returns_404_for_unknown_student`

### Suite de UI futura
Archivo recomendado cuando exista runner frontend: `frontend/src/pages/StudentsPage.test.tsx`

- render del formulario y tabla
- alta exitosa con limpieza del formulario
- visualizacion de errores de API
- cambio de estado desde boton `Activar/Desactivar`
- recalculo de contadores `Total` y `Activos`

## Datos y fixtures recomendados
- Factory reutilizable de estudiante con overrides para `document_id`, `email` e `is_active`.
- Dataset minimo:
  - 1 estudiante activo
  - 1 estudiante inactivo
  - 1 estudiante adicional para pruebas de duplicidad

## Criterio de aprobacion automatico del modulo
- Toda regla de negocio del backend para estudiantes debe quedar automatizada al menos a nivel servicio.
- Las validaciones de contrato deben estar cubiertas a nivel API.
- Las interacciones visuales pueden quedar como pendiente tecnica mientras no exista infraestructura de tests frontend, pero deben permanecer documentadas en este archivo.
