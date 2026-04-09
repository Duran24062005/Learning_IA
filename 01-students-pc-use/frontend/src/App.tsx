import { useEffect, useState } from 'react'
import './App.css'
import { getApiErrorMessage } from './utils/errorHandler'
import { StudentsPage } from './pages/StudentsPage'
import { ComputersPage } from './pages/ComputersPage'
import { AssignmentsPage } from './pages/AssignmentsPage'

type ViewKey = 'students' | 'computers' | 'assignments'

const views: { key: ViewKey; label: string; description: string }[] = [
  {
    key: 'students',
    label: 'Estudiantes',
    description: 'Registra y actualiza el estado de los campers activos en Cajasan.',
  },
  {
    key: 'computers',
    label: 'Computadores',
    description: 'Administra inventario, mantenimiento y equipos disponibles.',
  },
  {
    key: 'assignments',
    label: 'Asignaciones',
    description: 'Entrega equipos, procesa devoluciones y consulta historial.',
  },
]

function App() {
  const [activeView, setActiveView] = useState<ViewKey>('students')
  const [backendStatus, setBackendStatus] = useState<'checking' | 'online' | 'offline'>('checking')
  const [backendMessage, setBackendMessage] = useState('Conectando con la API...')

  useEffect(() => {
    const controller = new AbortController()

    fetch('http://localhost:8000/health', { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) {
          throw new Error('La API no respondió correctamente.')
        }
        return response.json()
      })
      .then(() => {
        setBackendStatus('online')
        setBackendMessage('API disponible en http://localhost:8000')
      })
      .catch((error: unknown) => {
        if (controller.signal.aborted) {
          return
        }
        setBackendStatus('offline')
        setBackendMessage(getApiErrorMessage(error))
      })

    return () => controller.abort()
  }, [])

  return (
    <div className="app-shell">
      <header className="hero-panel">
        <div>
          <p className="eyebrow">Campuslands · Control interno</p>
          <h1>Gestión de estudiantes y computadores</h1>
          <p className="hero-copy">
            Una consola operativa para registrar estudiantes, administrar equipos y
            controlar asignaciones activas e históricas.
          </p>
        </div>
        <div className={`status-card ${backendStatus}`}>
          <span className="status-dot" />
          <div>
            <strong>Estado del backend</strong>
            <p>{backendMessage}</p>
          </div>
        </div>
      </header>

      <nav className="view-switcher" aria-label="Secciones principales">
        {views.map((view) => (
          <button
            key={view.key}
            className={view.key === activeView ? 'active' : ''}
            onClick={() => setActiveView(view.key)}
            type="button"
          >
            <span>{view.label}</span>
            <small>{view.description}</small>
          </button>
        ))}
      </nav>

      <main className="main-content">
        {activeView === 'students' && <StudentsPage />}
        {activeView === 'computers' && <ComputersPage />}
        {activeView === 'assignments' && <AssignmentsPage />}
      </main>
    </div>
  )
}

export default App
