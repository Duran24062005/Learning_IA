import { useState } from 'react'
import { StudentForm } from '../components/students/StudentForm'
import { StudentsTable } from '../components/students/StudentsTable'
import { useStudents } from '../hooks/useStudents'
import { ErrorMessage } from '../components/common/ErrorMessage'
import { getApiErrorMessage } from '../utils/errorHandler'
import type { Student } from '../types'

export function StudentsPage() {
  const { students, loading, createStudent, updateStudent } = useStudents()
  const [pageError, setPageError] = useState<string | null>(null)

  const handleToggleStatus = async (student: Student) => {
    try {
      setPageError(null)
      await updateStudent(student.id, { is_active: !student.is_active })
    } catch (error) {
      setPageError(getApiErrorMessage(error))
    }
  }

  return (
    <section className="page-grid">
      <div className="page-header">
        <h2>Estudiantes</h2>
        <p>
          Registra campers, actualiza su estado operativo y mantén el directorio listo
          para las asignaciones.
        </p>
      </div>
      <div className="two-column">
        <article className="panel">
          <h3>Nuevo estudiante</h3>
          <StudentForm onSubmit={createStudent} />
        </article>
        <article className="panel">
          <div className="meta-list">
            <span className="meta-chip">Total: {students.length}</span>
            <span className="meta-chip">
              Activos: {students.filter((student) => student.is_active).length}
            </span>
          </div>
          <ErrorMessage message={pageError} />
          {loading ? (
            <div className="empty-state">Cargando estudiantes...</div>
          ) : (
            <StudentsTable students={students} onToggleStatus={handleToggleStatus} />
          )}
        </article>
      </div>
    </section>
  )
}
