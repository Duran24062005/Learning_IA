# Sistema de Gestión de Estudiantes y Computadores

Aplicación full stack para controlar qué computadores usan los campers dentro de las instalaciones de Cajasan. El proyecto quedó implementado como un MVP con:

- `backend/`: API REST con `FastAPI`, `SQLAlchemy` y `SQLite`
- `frontend/`: interfaz en `React + TypeScript + Vite`

## Qué resuelve esta versión

- Registro y actualización de estudiantes
- Registro y actualización de computadores
- Asignación de computadores a estudiantes activos
- Devolución de equipos y liberación automática del inventario
- Consulta de historial de asignaciones
- Vista operativa de disponibilidad y estados

## Estructura

```text
01-students-pc-use/
├── backend/
│   ├── app/
│   │   ├── api/v1/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    └── src/
```

## Requisitos

- Python 3.11+
- Node.js 20+
- Yarn

## Cómo ejecutar el backend

Desde `01-students-pc-use/backend`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

La API quedará disponible en `http://localhost:8000`.

### Endpoints principales

- `GET /health`
- `POST /api/v1/students`
- `GET /api/v1/students`
- `PATCH /api/v1/students/{student_id}`
- `POST /api/v1/computers`
- `GET /api/v1/computers`
- `PATCH /api/v1/computers/{computer_id}`
- `POST /api/v1/assignments`
- `GET /api/v1/assignments`
- `POST /api/v1/assignments/{assignment_id}/return`

## Cómo ejecutar el frontend

Desde `01-students-pc-use/frontend`:

```bash
yarn install
yarn dev
```

La interfaz quedará en `http://localhost:5173` y consulta la API en `http://localhost:8000`.

## Cómo ejecutar con Docker

Desde la raíz del repositorio (`IA/`):

```bash
docker compose up --build
```

Servicios expuestos:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`

Detalles de la dockerización:

- El frontend se compila y se sirve con `nginx`
- El backend corre con `uvicorn`
- La base SQLite se persiste en el volumen `students_pc_data`

Para detener los contenedores:

```bash
docker compose down
```

Para detenerlos y borrar el volumen de datos:

```bash
docker compose down -v
```

## Reglas de negocio implementadas

- No se puede asignar un computador que no esté `available`
- No se puede asignar un computador a un estudiante inactivo
- El estado `assigned` solo lo controla el flujo de asignaciones
- Al devolver un equipo, la asignación se cierra y el computador vuelve a `available`

## Pruebas backend

Desde `01-students-pc-use/backend`:

```bash
pytest
```

Las pruebas cubren:

- creación de estudiantes y computadores
- rechazo de duplicados
- asignación válida
- rechazo por estudiante inactivo
- rechazo por computador no disponible
- devolución de equipos
- consulta de historial
