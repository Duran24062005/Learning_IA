# Testeo Manual - Modulo de Asignaciones

## Objetivo del modulo
Validar el flujo manual de entrega y devolucion de equipos, asegurando que solo se asignen computadores disponibles a estudiantes activos, que el historial se mantenga consistente y que las devoluciones liberen el inventario correctamente.

## Precondiciones del entorno
- Backend disponible en `http://localhost:8000`.
- Frontend disponible en `http://localhost:5173`.
- Navegador con acceso a la vista `Asignaciones`.
- Contar con datos previos de estudiantes y computadores para ejecutar escenarios positivos y negativos.

## Datos base requeridos
- Al menos un estudiante activo.
- Al menos un estudiante inactivo.
- Al menos un computador disponible.
- Al menos un computador en mantenimiento.
- Si se quiere validar doble devolucion, al menos una asignacion cerrada o posibilidad de crearla dentro de la prueba.

## Criterio de aprobacion del modulo
- La asignacion solo puede realizarse con estudiantes activos y computadores disponibles.
- La UI filtra las opciones del formulario segun esas reglas.
- Una asignacion exitosa actualiza inventario, historial y contadores.
- La devolucion cierra la asignacion y libera el computador.
- El sistema evita operaciones invalidas o repetidas.

## Estructura de casos
Cada caso incluye `ID`, `Escenario`, `Precondiciones`, `Datos de prueba`, `Pasos` y `Resultado esperado`.

---

## Caso ASG-01
**Escenario:** Creacion exitosa de una asignacion valida.

**Precondiciones**
- Existir al menos un estudiante activo.
- Existir al menos un computador disponible.
- Estar en la vista `Asignaciones`.

**Datos de prueba**
- Estudiante activo registrado.
- Computador disponible registrado.
- Observaciones: `Entrega inicial QA`.

**Pasos**
1. Seleccionar un estudiante activo en `Estudiante activo`.
2. Seleccionar un computador disponible en `Computador disponible`.
3. Ingresar una observacion opcional.
4. Hacer clic en `Asignar computador`.

**Resultado esperado**
- La asignacion se registra correctamente.
- El formulario se limpia despues del envio.
- El nuevo movimiento aparece en la tabla de historial.
- La columna `Devuelto` queda vacia o nula para la nueva fila.
- El contador `Historial` aumenta en 1.
- El contador `Activas` aumenta en 1.

---

## Caso ASG-02
**Escenario:** Visibilidad exclusiva de estudiantes activos en el selector.

**Precondiciones**
- Tener al menos un estudiante activo y uno inactivo.

**Datos de prueba**
- No aplica.

**Pasos**
1. Abrir el selector `Estudiante activo`.
2. Revisar las opciones listadas.

**Resultado esperado**
- Solo aparecen estudiantes con estado activo.
- Los estudiantes inactivos no deben estar disponibles para seleccion.

---

## Caso ASG-03
**Escenario:** Visibilidad exclusiva de computadores disponibles en el selector.

**Precondiciones**
- Tener al menos un computador disponible y uno en mantenimiento o asignado.

**Datos de prueba**
- No aplica.

**Pasos**
1. Abrir el selector `Computador disponible`.
2. Revisar las opciones listadas.

**Resultado esperado**
- Solo aparecen computadores en estado `available`.
- Los equipos en mantenimiento o asignados no aparecen como opcion.

---

## Caso ASG-04
**Escenario:** Bloqueo operativo cuando no hay estudiantes activos o computadores disponibles.

**Precondiciones**
- No tener estudiantes activos disponibles para asignar, o no tener computadores disponibles.

**Datos de prueba**
- No aplica.

**Pasos**
1. Dejar el sistema sin estudiantes activos seleccionables o sin computadores disponibles.
2. Abrir la vista `Asignaciones`.
3. Revisar el boton `Asignar computador`.

**Resultado esperado**
- El boton aparece deshabilitado.
- La UI no permite intentar una asignacion sin opciones validas.

---

## Caso ASG-05
**Escenario:** Cambio automatico del computador a estado asignado.

**Precondiciones**
- Haber creado una asignacion activa en la sesion actual.

**Datos de prueba**
- No aplica.

**Pasos**
1. Crear una asignacion valida.
2. Ir a la vista `Computadores`.
3. Ubicar el equipo recien asignado.

**Resultado esperado**
- El computador aparece con estado `assigned`.
- Sus acciones manuales de cambio de estado quedan deshabilitadas.
- El equipo deja de estar contado como disponible.

---

## Caso ASG-06
**Escenario:** Reflejo del movimiento en historial y contadores.

**Precondiciones**
- Haber creado una o mas asignaciones validas.

**Datos de prueba**
- No aplica.

**Pasos**
1. Abrir la vista `Asignaciones`.
2. Revisar la nueva fila en la tabla.
3. Verificar columnas de estudiante, equipo, fecha de asignacion, estado y notas.
4. Revisar contadores `Historial` y `Activas`.

**Resultado esperado**
- La fila contiene el estudiante correcto y el computador correcto.
- La fecha de asignacion es visible.
- El estado del equipo en la fila corresponde a `assigned`.
- Los contadores reflejan correctamente el total historico y las activas.

---

## Caso ASG-07
**Escenario:** Devolucion exitosa de una asignacion activa.

**Precondiciones**
- Existir al menos una asignacion activa.

**Datos de prueba**
- Utilizar una fila con boton `Registrar devolucion`.

**Pasos**
1. Localizar una asignacion activa.
2. Hacer clic en `Registrar devolucion`.

**Resultado esperado**
- La devolucion se registra correctamente.
- La columna `Devuelto` muestra una fecha.
- El boton cambia a `Cerrada` y queda deshabilitado.
- El contador `Activas` disminuye en 1.

---

## Caso ASG-08
**Escenario:** Liberacion automatica del computador despues de devolverlo.

**Precondiciones**
- Haber registrado una devolucion exitosa.

**Datos de prueba**
- No aplica.

**Pasos**
1. Registrar la devolucion de una asignacion activa.
2. Ir a la vista `Computadores`.
3. Revisar el estado del computador devuelto.
4. Volver a `Asignaciones` y abrir el selector de computadores disponibles.

**Resultado esperado**
- El computador vuelve a estado `available`.
- El contador de disponibles aumenta en el modulo `Computadores`.
- El equipo vuelve a aparecer como opcion seleccionable en nuevas asignaciones.

---

## Caso ASG-09
**Escenario:** Rechazo al intentar asignar un estudiante inactivo.

**Precondiciones**
- Tener al menos un estudiante inactivo registrado.
- Contar con acceso a una validacion integrada UI + sistema.

**Datos de prueba**
- Estudiante inactivo existente.
- Computador disponible existente.

**Pasos**
1. Confirmar que el estudiante inactivo no aparece en el selector de la UI.
2. Si se desea validacion adicional, intentar forzar la operacion via llamada manual al endpoint `POST /api/v1/assignments` usando el `student_id` inactivo y un computador disponible.

**Resultado esperado**
- La UI previene la seleccion del estudiante inactivo.
- Si se fuerza la llamada al backend, la operacion debe ser rechazada.
- No se crea ninguna asignacion invalida.

---

## Caso ASG-10
**Escenario:** Rechazo al intentar asignar un computador no disponible.

**Precondiciones**
- Tener al menos un computador en mantenimiento o ya asignado.
- Contar con acceso a una validacion integrada UI + sistema.

**Datos de prueba**
- Estudiante activo existente.
- Computador no disponible existente.

**Pasos**
1. Confirmar que el computador no disponible no aparece en el selector de la UI.
2. Si se desea validacion adicional, intentar forzar la operacion via `POST /api/v1/assignments` usando un computador no disponible.

**Resultado esperado**
- La UI no ofrece el computador como opcion.
- Si se fuerza la llamada al backend, la operacion es rechazada.
- No se crea una asignacion invalida.

---

## Caso ASG-11
**Escenario:** Rechazo de doble devolucion sobre una asignacion cerrada.

**Precondiciones**
- Tener una asignacion ya devuelta.

**Datos de prueba**
- Asignacion cerrada existente.

**Pasos**
1. Localizar una fila cerrada en la tabla.
2. Verificar el estado del boton de accion.
3. Si se desea validacion adicional, intentar invocar manualmente `POST /api/v1/assignments/{assignment_id}/return` sobre esa asignacion.

**Resultado esperado**
- En la UI el boton aparece como `Cerrada` y no permite una segunda devolucion.
- Si se fuerza la llamada al backend, la operacion debe ser rechazada.
- La fecha y notas de la asignacion cerrada no se alteran.

---

## Caso ASG-12
**Escenario:** Regresion ligera del ciclo completo asignar y devolver.

**Precondiciones**
- Tener un estudiante activo y un computador disponible.

**Datos de prueba**
- Observaciones iniciales: `Ciclo completo QA`

**Pasos**
1. Crear una asignacion valida.
2. Verificar en `Computadores` que el equipo quede en `assigned`.
3. Volver a `Asignaciones` y registrar la devolucion.
4. Verificar en `Computadores` que el equipo regrese a `available`.
5. Confirmar en `Asignaciones` que la fila quede cerrada.

**Resultado esperado**
- El flujo completo se ejecuta sin errores.
- El historial conserva la asignacion y la devolucion en la misma fila.
- El inventario termina consistente con el estado final del equipo.
