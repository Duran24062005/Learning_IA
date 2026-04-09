import type { Student } from '../../types'
import { formatDate } from '../../utils/formatDate'

interface StudentsTableProps {
  students: Student[]
  onToggleStatus: (student: Student) => Promise<void>
}

export function StudentsTable({ students, onToggleStatus }: StudentsTableProps) {
  if (students.length === 0) {
    return <div className="empty-state">Aún no hay estudiantes registrados.</div>
  }

  return (
    <div className="table-wrap">
      <table className="data-table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Documento</th>
            <th>Correo</th>
            <th>Estado</th>
            <th>Registro</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id}>
              <td>{student.full_name}</td>
              <td>{student.document_id}</td>
              <td>{student.email}</td>
              <td>{student.is_active ? 'Activo' : 'Inactivo'}</td>
              <td>{formatDate(student.created_at)}</td>
              <td>
                <button
                  className="secondary-button"
                  onClick={() => void onToggleStatus(student)}
                  type="button"
                >
                  {student.is_active ? 'Desactivar' : 'Activar'}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
