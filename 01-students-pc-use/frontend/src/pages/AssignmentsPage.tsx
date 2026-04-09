import { useEffect, useState } from 'react'
import { AssignmentForm } from '../components/assignments/AssignmentForm'
import { AssignmentsTable } from '../components/assignments/AssignmentsTable'
import { ErrorMessage } from '../components/common/ErrorMessage'
import { useAssignments } from '../hooks/useAssignments'
import { useComputers } from '../hooks/useComputers'
import { useStudents } from '../hooks/useStudents'
import { getApiErrorMessage } from '../utils/errorHandler'
import type { Assignment } from '../types'

export function AssignmentsPage() {
  const studentsState = useStudents()
  const computersState = useComputers()
  const assignmentsState = useAssignments()
  const [pageError, setPageError] = useState<string | null>(null)

  useEffect(() => {
    if (!assignmentsState.loading) {
      void studentsState.refreshStudents()
      void computersState.refreshComputers()
    }
  }, [assignmentsState.loading])

  const refreshAll = async () => {
    await Promise.all([
      studentsState.refreshStudents(),
      computersState.refreshComputers(),
      assignmentsState.refreshAssignments(),
    ])
  }

  const handleCreateAssignment = async (payload: {
    student_id: string
    computer_id: string
    notes: string
  }) => {
    try {
      setPageError(null)
      await assignmentsState.createAssignment(payload)
      await Promise.all([studentsState.refreshStudents(), computersState.refreshComputers()])
    } catch (error) {
      throw error
    }
  }

  const handleReturn = async (assignment: Assignment) => {
    try {
      setPageError(null)
      await assignmentsState.returnAssignment(assignment.id, {
        notes: 'Equipo devuelto desde consola operativa',
      })
      await refreshAll()
    } catch (error) {
      setPageError(getApiErrorMessage(error))
    }
  }

  const activeAssignments = assignmentsState.assignments.filter(
    (assignment) => assignment.returned_at === null,
  )

  return (
    <section className="page-grid">
      <div className="page-header">
        <h2>Asignaciones</h2>
        <p>
          Entrega equipos a estudiantes activos, registra devoluciones y consulta el
          historial completo de movimientos.
        </p>
      </div>
      <div className="two-column">
        <article className="panel">
          <h3>Nueva asignación</h3>
          <AssignmentForm
            students={studentsState.students}
            computers={computersState.computers}
            onSubmit={handleCreateAssignment}
          />
        </article>
        <article className="panel">
          <div className="meta-list">
            <span className="meta-chip">Historial: {assignmentsState.assignments.length}</span>
            <span className="meta-chip">Activas: {activeAssignments.length}</span>
          </div>
          <ErrorMessage message={pageError} />
          {assignmentsState.loading ? (
            <div className="empty-state">Cargando asignaciones...</div>
          ) : (
            <AssignmentsTable
              assignments={assignmentsState.assignments}
              onReturn={handleReturn}
            />
          )}
        </article>
      </div>
    </section>
  )
}
