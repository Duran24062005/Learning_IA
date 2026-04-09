# Plan de Implementación: Sistema de Gestión de Estudiantes y Computadores

## Resumen
Construir una primera versión funcional dentro de `01-students-pc-use` reutilizando el frontend actual de Vite + React + TypeScript y agregando un backend con FastAPI. Esta fase cubrirá el MVP completo del dominio: estudiantes, computadores, asignaciones, devoluciones, listados operativos e historial.  
Por decisión tomada en esta planificación, la primera versión usará `SQLite` para acelerar el arranque local, aunque el README menciona `PostgreSQL`; la arquitectura quedará preparada para migrar luego sin rehacer la lógica.

## Cambios de Implementación
- Crear `backend/` con arquitectura por capas alineada al README: `api`, `core`, `db`, `models`, `schemas`, `services`, más `main.py`.
- Modelar las entidades `Student`, `Computer` y `Assignment` con reglas de negocio explícitas:
  - `Student`: nombre, documento único, email único, estado activo.
  - `Computer`: serial único, marca, modelo, estado (`available`, `assigned`, `maintenance`).
  - `Assignment`: relación estudiante-computador con `assigned_at`, `returned_at` y `notes`.
- Implementar servicios para encapsular reglas críticas:
  - No permitir asignar un computador que no esté `available`.
  - No permitir asignar a un estudiante inactivo.
  - No permitir más de una asignación activa por computador.
  - Al devolver, cerrar la asignación activa y cambiar el computador a `available`.
- Exponer endpoints REST para el MVP:
  - `POST/GET/PATCH` de estudiantes.
  - `POST/GET/PATCH` de computadores.
  - `POST` para asignar computador.
  - `POST` o `PATCH` para devolución.
  - `GET` para computadores disponibles.
  - `GET` para historial por estudiante y/o computador.
- Mantener el backend simple en esta fase:
  - Sin autenticación.
  - Sin Alembic todavía, salvo que durante implementación se vea necesario para no bloquear el flujo.
  - Configuración por `.env`, con URL de base de datos SQLite por defecto.
- Reemplazar el template visual de `frontend/` por una app real con React:
  - Estructura por `pages`, `components`, `api`, `hooks` y `utils`, siguiendo el README pero en TypeScript.
  - Pantallas mínimas: estudiantes, computadores y asignaciones.
  - Formularios para crear estudiantes/computadores y para asignar/devolver.
  - Tablas o listas para ver estado actual e historial.
  - Cliente HTTP centralizado para consumir FastAPI.
- Ajustar la UX al flujo operativo real:
  - Mostrar estados del computador con badges.
  - Bloquear acciones inválidas desde UI cuando sea posible.
  - Mostrar errores de validación y reglas de negocio devueltos por la API.
- Dejar preparado el proyecto para ejecución local clara:
  - Backend con comando de desarrollo documentado.
  - Frontend con `yarn dev`.
  - README actualizado con pasos reales de instalación y arranque de ambos lados.

## APIs, Interfaces y Tipos Públicos
- API backend base: prefijo versionado, preferiblemente `/api/v1`.
- Esquemas de entrada/salida:
  - `StudentCreate`, `StudentUpdate`, `StudentOut`
  - `ComputerCreate`, `ComputerUpdate`, `ComputerOut`
  - `AssignmentCreate`, `AssignmentOut`, `AssignmentReturn`
- Tipos frontend alineados con esos contratos para evitar duplicar formas inconsistentes.
- Enumeración compartida por contrato para estado de computador: `available | assigned | maintenance`.

## Plan de Pruebas
- Pruebas backend por casos de uso principales:
  - crear estudiante y computador correctamente;
  - rechazar duplicados de `document_id`, `email` y `serial_number`;
  - asignar computador disponible a estudiante activo;
  - rechazar asignación de equipo no disponible;
  - rechazar asignación a estudiante inactivo;
  - devolver equipo y liberar estado;
  - consultar historial y listados operativos.
- Validación manual frontend:
  - crear registros desde formularios;
  - ver reflejo inmediato en tablas;
  - asignar y devolver sin recargar flujo completo;
  - visualizar mensajes de error ante reglas incumplidas.
- Verificación integrada:
  - frontend consumiendo backend localmente;
  - arranque limpio desde cero siguiendo solo el README actualizado.

## Supuestos y Decisiones Cerradas
- Esta fase es un MVP funcional completo del dominio, sin autenticación.
- Se reutiliza `frontend/` actual como base técnica, pero se reemplaza su contenido de plantilla.
- Se implementa en `React + TypeScript + Vite` y `FastAPI`.
- Se usará `SQLite` en esta primera entrega como decisión explícita, dejando el acceso a datos abstraído para migrar luego a PostgreSQL.
- No se contemplan roles, permisos, dashboard analítico ni despliegue productivo en esta fase.
