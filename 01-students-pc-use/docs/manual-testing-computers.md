# Testeo Manual - Modulo de Computadores

## Objetivo del modulo
Validar el flujo manual de inventario de computadores, asegurando que el sistema permita registrar equipos, reflejar su estado operativo y respetar las restricciones funcionales sobre disponibilidad, mantenimiento y asignacion.

## Precondiciones del entorno
- Backend disponible en `http://localhost:8000`.
- Frontend disponible en `http://localhost:5173`.
- Navegador con acceso a la vista `Computadores`.
- Base de datos operativa y sin errores visibles al cargar la aplicacion.

## Datos base requeridos
- Al menos dos seriales no usados para pruebas positivas.
- Al menos un computador disponible para pruebas de cambio de estado.
- Si se van a validar restricciones integradas, al menos un computador debe poder ser usado luego en una asignacion.

## Criterio de aprobacion del modulo
- Los computadores se registran con los datos correctos.
- La tabla y el contador de disponibles coinciden con el estado real del inventario.
- El sistema rechaza seriales duplicados.
- La UI permite cambiar estados manuales validos y bloquea el estado `assigned`.
- Los cambios de estado persisten al recargar y no generan inconsistencias visuales.

## Estructura de casos
Cada caso incluye `ID`, `Escenario`, `Precondiciones`, `Datos de prueba`, `Pasos` y `Resultado esperado`.

---

## Caso COM-01
**Escenario:** Registro exitoso de computador disponible.

**Precondiciones**
- Estar en la vista `Computadores`.
- El serial no debe existir previamente.

**Datos de prueba**
- Serial: `CJS-QA-001`
- Marca: `Dell`
- Modelo: `Latitude 5420`
- Estado inicial: `Disponible`

**Pasos**
1. Completar el formulario `Nuevo computador`.
2. Dejar `Estado inicial` en `Disponible`.
3. Hacer clic en `Registrar computador`.

**Resultado esperado**
- El formulario se limpia al guardar.
- El equipo aparece en la tabla.
- El badge de estado muestra `available` o su equivalente visual de disponible.
- El contador `Total` aumenta en 1.
- El contador `Disponibles` aumenta en 1.

---

## Caso COM-02
**Escenario:** Registro exitoso de computador en mantenimiento.

**Precondiciones**
- Estar en la vista `Computadores`.
- El serial no debe existir previamente.

**Datos de prueba**
- Serial: `CJS-QA-002`
- Marca: `Lenovo`
- Modelo: `ThinkPad E14`
- Estado inicial: `Mantenimiento`

**Pasos**
1. Completar el formulario con los datos definidos.
2. Seleccionar `Mantenimiento` en `Estado inicial`.
3. Hacer clic en `Registrar computador`.

**Resultado esperado**
- El equipo se registra correctamente.
- La fila aparece con estado de mantenimiento.
- El contador `Total` aumenta en 1.
- El contador `Disponibles` no aumenta.

---

## Caso COM-03
**Escenario:** Validacion de campos requeridos en el formulario.

**Precondiciones**
- Estar en la vista `Computadores`.

**Datos de prueba**
- Dejar vacios los campos `Serial`, `Marca` o `Modelo`.

**Pasos**
1. Intentar enviar el formulario dejando vacio `Serial`.
2. Repetir dejando vacio `Marca`.
3. Repetir dejando vacio `Modelo`.

**Resultado esperado**
- El navegador impide el envio del formulario mientras falte un campo requerido.
- No se crean registros parciales.
- No cambian tabla ni contadores.

---

## Caso COM-04
**Escenario:** Rechazo de serial duplicado.

**Precondiciones**
- Existir un computador previamente creado con serial conocido.

**Datos de prueba**
- Serial: usar un serial ya registrado
- Marca: `HP`
- Modelo: `ProBook 440`

**Pasos**
1. Completar el formulario con un serial ya existente.
2. Hacer clic en `Registrar computador`.

**Resultado esperado**
- La operacion falla.
- Se muestra mensaje de error en el formulario.
- El equipo duplicado no aparece en la tabla.
- Los contadores permanecen sin cambios.

---

## Caso COM-05
**Escenario:** Visualizacion correcta del inventario y contador de disponibles.

**Precondiciones**
- Tener al menos un computador disponible y uno en mantenimiento.

**Datos de prueba**
- No aplica.

**Pasos**
1. Abrir la vista `Computadores`.
2. Revisar el contador `Total`.
3. Revisar el contador `Disponibles`.
4. Verificar columnas `Serial`, `Marca`, `Modelo`, `Estado`, `Registro` y `Acciones`.

**Resultado esperado**
- `Total` coincide con el numero de filas.
- `Disponibles` coincide con la cantidad de equipos en estado `available`.
- Cada fila muestra informacion completa y coherente.

---

## Caso COM-06
**Escenario:** Cambio manual de disponible a mantenimiento.

**Precondiciones**
- Existir al menos un computador en estado `available`.

**Datos de prueba**
- Seleccionar un computador disponible.

**Pasos**
1. Localizar un computador disponible.
2. Hacer clic en `Mantenimiento`.

**Resultado esperado**
- El estado cambia a mantenimiento.
- El contador `Disponibles` disminuye en 1.
- El cambio se refleja inmediatamente en la tabla.
- No se muestran errores.

---

## Caso COM-07
**Escenario:** Cambio manual de mantenimiento a disponible.

**Precondiciones**
- Existir al menos un computador en mantenimiento.

**Datos de prueba**
- Seleccionar un computador en mantenimiento.

**Pasos**
1. Localizar un computador en mantenimiento.
2. Hacer clic en `Marcar disponible`.

**Resultado esperado**
- El estado cambia a disponible.
- El contador `Disponibles` aumenta en 1.
- La tabla refleja el cambio sin duplicar filas.

---

## Caso COM-08
**Escenario:** Restriccion funcional de estados operativos validos.

**Precondiciones**
- Estar en la vista `Computadores`.

**Datos de prueba**
- No aplica.

**Pasos**
1. Revisar el formulario de creacion.
2. Revisar las acciones disponibles en la tabla.

**Resultado esperado**
- El formulario solo permite seleccionar `Disponible` o `Mantenimiento`.
- La tabla solo ofrece `Marcar disponible` y `Mantenimiento`.
- No existe una accion manual para establecer el estado `assigned`.

---

## Caso COM-09
**Escenario:** Persistencia del cambio de estado tras recargar.

**Precondiciones**
- Haber cambiado el estado de al menos un computador durante la sesion actual.

**Datos de prueba**
- No aplica.

**Pasos**
1. Cambiar el estado de un equipo.
2. Recargar la pagina.
3. Revisar nuevamente la fila del equipo y el contador de disponibles.

**Resultado esperado**
- El estado se conserva despues de recargar.
- Los contadores mantienen el valor correcto.
- No hay reversiones ni desalineacion visual.

---

## Caso COM-10
**Escenario:** Regresion ligera entre altas y cambios de estado.

**Precondiciones**
- Vista `Computadores` disponible.

**Datos de prueba**
- Serial 1: `CJS-QA-003`
- Serial 2: `CJS-QA-004`

**Pasos**
1. Registrar un equipo disponible.
2. Registrar un equipo en mantenimiento.
3. Cambiar el primero a mantenimiento.
4. Cambiar el segundo a disponible.
5. Revisar el inventario final.

**Resultado esperado**
- Todos los cambios afectan solo al registro correspondiente.
- El contador `Disponibles` refleja el resultado final real.
- No se presentan errores ni estados cruzados.

---

## Caso COM-11
**Escenario:** Validacion integrada de restriccion sobre equipo asignado.

**Precondiciones**
- Existir un computador que haya sido asignado desde el modulo `Asignaciones`.
- Estar en la vista `Computadores`.

**Datos de prueba**
- Usar un computador con asignacion activa.

**Pasos**
1. Crear una asignacion activa para un computador disponible desde la vista `Asignaciones`.
2. Volver a la vista `Computadores`.
3. Ubicar el computador asignado.
4. Revisar el estado de los botones `Marcar disponible` y `Mantenimiento`.

**Resultado esperado**
- El equipo aparece en estado `assigned`.
- Los botones manuales aparecen deshabilitados.
- La UI evita el cambio manual de estado mientras exista una asignacion activa.
