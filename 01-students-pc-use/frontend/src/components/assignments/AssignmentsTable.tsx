import { StatusBadge } from '../common/StatusBadge'
import type { Assignment } from '../../types'
import { formatDate } from '../../utils/formatDate'

interface AssignmentsTableProps {
  assignments: Assignment[]
  onReturn: (assignment: Assignment) => Promise<void>
}

export function AssignmentsTable({ assignments, onReturn }: AssignmentsTableProps) {
  if (assignments.length === 0) {
    return <div className="empty-state">No hay asignaciones registradas todavía.</div>
  }

  return (
    <div className="table-wrap">
      <table className="data-table">
        <thead>
          <tr>
            <th>Estudiante</th>
            <th>Equipo</th>
            <th>Asignado</th>
            <th>Devuelto</th>
            <th>Estado</th>
            <th>Notas</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          {assignments.map((assignment) => {
            const isActive = assignment.returned_at === null

            return (
              <tr key={assignment.id}>
                <td>
                  <strong>{assignment.student.full_name}</strong>
                  <div>{assignment.student.document_id}</div>
                </td>
                <td>
                  <strong>{assignment.computer.serial_number}</strong>
                  <div>
                    {assignment.computer.brand} {assignment.computer.model}
                  </div>
                </td>
                <td>{formatDate(assignment.assigned_at)}</td>
                <td>{formatDate(assignment.returned_at)}</td>
                <td>
                  <StatusBadge status={assignment.computer.status} />
                </td>
                <td>{assignment.notes || 'Sin observaciones'}</td>
                <td>
                  <button
                    className={isActive ? 'danger-button' : 'secondary-button'}
                    disabled={!isActive}
                    onClick={() => void onReturn(assignment)}
                    type="button"
                  >
                    {isActive ? 'Registrar devolución' : 'Cerrada'}
                  </button>
                </td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
  )
}
