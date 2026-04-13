# Testeo Manual - Modulo de Estudiantes

## Objetivo del modulo
Validar el flujo manual de gestion de estudiantes desde la interfaz operativa, asegurando que el sistema permita registrar campers, listarlos, cambiar su estado y aplicar las restricciones de unicidad y validacion definidas por el backend.

## Precondiciones del entorno
- Backend disponible en `http://localhost:8000`.
- Frontend disponible en `http://localhost:5173`.
- Base de datos accesible y sin errores visibles al cargar la aplicacion.
- Navegador con acceso a la aplicacion y, si aplica, a la pestaña de red para revisar respuestas HTTP.

## Datos base requeridos
- Tener acceso a la vista `Estudiantes`.
- Contar con al menos dos correos y dos documentos no usados para pruebas positivas.
- Contar con un estudiante previamente creado para pruebas de edicion de estado y duplicados.

## Criterio de aprobacion del modulo
- Los estudiantes se registran y aparecen en la tabla con los datos correctos.
- El contador total y el contador de activos reflejan el estado real de la tabla.
- El sistema impide registros duplicados por documento o correo.
- La UI refleja correctamente la activacion e inactivacion de estudiantes.
- Las validaciones requeridas del formulario y del backend se presentan sin comportamientos inconsistentes.

## Estructura de casos
Cada caso incluye `ID`, `Escenario`, `Precondiciones`, `Datos de prueba`, `Pasos` y `Resultado esperado`.

---

## Caso STU-01
**Escenario:** Registro exitoso de estudiante activo.

**Precondiciones**
- Estar en la vista `Estudiantes`.
- No existir previamente el documento ni el correo que se van a usar.

**Datos de prueba**
- Nombre completo: `Laura Martinez`
- Documento: `1098765432`
- Correo: `laura.martinez.qa1@campuslands.com`
- Estado: `Activo`

**Pasos**
1. Completar el formulario `Nuevo estudiante` con los datos indicados.
2. Confirmar que el selector `Estado` quede en `Activo`.
3. Hacer clic en `Registrar estudiante`.

**Resultado esperado**
- El formulario se limpia despues de guardar.
- El nuevo estudiante aparece en la tabla.
- La fila muestra `Activo` en la columna de estado.
- El contador `Total` aumenta en 1.
- El contador `Activos` aumenta en 1.
- No se muestra mensaje de error.

---

## Caso STU-02
**Escenario:** Registro exitoso de estudiante inactivo.

**Precondiciones**
- Estar en la vista `Estudiantes`.
- No existir previamente el documento ni el correo que se van a usar.

**Datos de prueba**
- Nombre completo: `Carlos Perez`
- Documento: `1098765433`
- Correo: `carlos.perez.qa1@campuslands.com`
- Estado: `Inactivo`

**Pasos**
1. Completar el formulario con los datos definidos.
2. Seleccionar `Inactivo` en el campo `Estado`.
3. Hacer clic en `Registrar estudiante`.

**Resultado esperado**
- El estudiante se registra correctamente.
- La fila aparece con estado `Inactivo`.
- El contador `Total` aumenta en 1.
- El contador `Activos` no aumenta.
- No se presenta error visual ni inconsistencia en la tabla.

---

## Caso STU-03
**Escenario:** Validacion de campos requeridos en el formulario.

**Precondiciones**
- Estar en la vista `Estudiantes`.

**Datos de prueba**
- Dejar vacios uno o varios de los campos `Nombre completo`, `Documento` y `Correo`.

**Pasos**
1. Abrir el formulario `Nuevo estudiante`.
2. Intentar enviar el formulario dejando vacio `Nombre completo`.
3. Repetir la prueba dejando vacio `Documento`.
4. Repetir la prueba dejando vacio `Correo`.

**Resultado esperado**
- El navegador impide el envio del formulario cuando falta un campo requerido.
- No se crea ningun registro parcial.
- No cambian los contadores ni la tabla.

---

## Caso STU-04
**Escenario:** Validacion del formato de correo electronico.

**Precondiciones**
- Estar en la vista `Estudiantes`.

**Datos de prueba**
- Nombre completo: `Correo Invalido`
- Documento: `1098765434`
- Correo: `correo-invalido`

**Pasos**
1. Completar el formulario con el correo invalido.
2. Hacer clic en `Registrar estudiante`.

**Resultado esperado**
- El navegador bloquea el envio por formato de correo invalido.
- No se crea el estudiante.
- No se altera el listado.

---

## Caso STU-05
**Escenario:** Rechazo de documento duplicado.

**Precondiciones**
- Existir un estudiante con documento ya registrado.
- Estar en la vista `Estudiantes`.

**Datos de prueba**
- Nombre completo: `Documento Duplicado`
- Documento: usar un documento ya existente
- Correo: `doc.duplicado.qa1@campuslands.com`

**Pasos**
1. Completar el formulario con un documento ya registrado y un correo nuevo.
2. Hacer clic en `Registrar estudiante`.

**Resultado esperado**
- La operacion falla.
- Se muestra un mensaje de error visible en el formulario.
- El estudiante no aparece en la tabla.
- Los contadores no cambian.
- Si se inspecciona la respuesta del sistema, debe corresponder a una restriccion de unicidad por documento.

---

## Caso STU-06
**Escenario:** Rechazo de correo duplicado.

**Precondiciones**
- Existir un estudiante con correo ya registrado.
- Estar en la vista `Estudiantes`.

**Datos de prueba**
- Nombre completo: `Correo Duplicado`
- Documento: `1098765435`
- Correo: usar un correo ya existente

**Pasos**
1. Completar el formulario con un documento nuevo y un correo ya registrado.
2. Hacer clic en `Registrar estudiante`.

**Resultado esperado**
- La operacion falla.
- Se muestra un mensaje de error visible en el formulario.
- El registro no se crea.
- La tabla y los contadores permanecen sin cambios.

---

## Caso STU-07
**Escenario:** Visualizacion correcta de tabla y contadores.

**Precondiciones**
- Tener al menos un estudiante activo y uno inactivo registrados.

**Datos de prueba**
- No aplica.

**Pasos**
1. Abrir la vista `Estudiantes`.
2. Revisar el contador `Total`.
3. Revisar el contador `Activos`.
4. Verificar que cada fila muestre nombre, documento, correo, estado, fecha de registro y accion.

**Resultado esperado**
- El contador `Total` coincide con el numero de filas mostradas.
- El contador `Activos` coincide con la cantidad de filas con estado `Activo`.
- La tabla presenta toda la informacion esperada sin columnas vacias injustificadas.

---

## Caso STU-08
**Escenario:** Desactivacion de un estudiante desde la tabla.

**Precondiciones**
- Existir al menos un estudiante activo.
- Estar en la vista `Estudiantes`.

**Datos de prueba**
- Seleccionar un estudiante con estado `Activo`.

**Pasos**
1. Localizar un estudiante activo en la tabla.
2. Hacer clic en `Desactivar`.

**Resultado esperado**
- La fila cambia a estado `Inactivo`.
- El boton cambia a `Activar`.
- El contador `Activos` disminuye en 1.
- El estudiante sigue apareciendo en el listado.
- No se muestran errores.

---

## Caso STU-09
**Escenario:** Activacion de un estudiante desde la tabla.

**Precondiciones**
- Existir al menos un estudiante inactivo.
- Estar en la vista `Estudiantes`.

**Datos de prueba**
- Seleccionar un estudiante con estado `Inactivo`.

**Pasos**
1. Localizar un estudiante inactivo en la tabla.
2. Hacer clic en `Activar`.

**Resultado esperado**
- La fila cambia a estado `Activo`.
- El boton cambia a `Desactivar`.
- El contador `Activos` aumenta en 1.
- El listado se mantiene consistente.

---

## Caso STU-10
**Escenario:** Persistencia del estado despues de recargar la vista.

**Precondiciones**
- Haber activado o desactivado al menos un estudiante durante la sesion actual.

**Datos de prueba**
- No aplica.

**Pasos**
1. Cambiar el estado de un estudiante desde la tabla.
2. Recargar la pagina del navegador.
3. Volver a revisar la fila modificada y los contadores.

**Resultado esperado**
- El estado actualizado se conserva despues de recargar.
- Los contadores mantienen los valores correctos.
- No aparecen reversiones de estado ni duplicados.

---

## Caso STU-11
**Escenario:** Regresion ligera sobre convivencia de estudiantes activos e inactivos.

**Precondiciones**
- Tener varios estudiantes registrados con estados mixtos.

**Datos de prueba**
- No aplica.

**Pasos**
1. Crear un estudiante activo.
2. Crear un estudiante inactivo.
3. Desactivar uno activo.
4. Activar uno inactivo.
5. Verificar el estado final de todas las filas involucradas.

**Resultado esperado**
- Cada cambio se refleja solo en el estudiante afectado.
- Los contadores se actualizan de forma incremental y correcta.
- No se alteran otros registros de manera lateral.
