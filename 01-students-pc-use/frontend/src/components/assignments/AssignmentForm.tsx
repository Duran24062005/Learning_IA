import { useMemo, useState, type FormEvent } from 'react'
import { ErrorMessage } from '../common/ErrorMessage'
import type {
  AssignmentPayload,
  Computer,
  Student,
} from '../../types'
import { getApiErrorMessage } from '../../utils/errorHandler'

interface AssignmentFormProps {
  students: Student[]
  computers: Computer[]
  onSubmit: (payload: AssignmentPayload) => Promise<void>
}

const initialForm: AssignmentPayload = {
  student_id: '',
  computer_id: '',
  notes: '',
}

export function AssignmentForm({
  students,
  computers,
  onSubmit,
}: AssignmentFormProps) {
  const [form, setForm] = useState<AssignmentPayload>(initialForm)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const availableStudents = useMemo(
    () => students.filter((student) => student.is_active),
    [students],
  )
  const availableComputers = useMemo(
    () => computers.filter((computer) => computer.status === 'available'),
    [computers],
  )

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setSaving(true)
    setError(null)

    try {
      await onSubmit(form)
      setForm(initialForm)
    } catch (submissionError) {
      setError(getApiErrorMessage(submissionError))
    } finally {
      setSaving(false)
    }
  }

  return (
    <form className="stack" onSubmit={handleSubmit}>
      <ErrorMessage message={error} />
      <div className="field">
        <label htmlFor="student_id">Estudiante activo</label>
        <select
          id="student_id"
          required
          value={form.student_id}
          onChange={(event) =>
            setForm((current) => ({ ...current, student_id: event.target.value }))
          }
        >
          <option value="">Selecciona un estudiante</option>
          {availableStudents.map((student) => (
            <option key={student.id} value={student.id}>
              {student.full_name} · {student.document_id}
            </option>
          ))}
        </select>
      </div>
      <div className="field">
        <label htmlFor="computer_id">Computador disponible</label>
        <select
          id="computer_id"
          required
          value={form.computer_id}
          onChange={(event) =>
            setForm((current) => ({ ...current, computer_id: event.target.value }))
          }
        >
          <option value="">Selecciona un equipo</option>
          {availableComputers.map((computer) => (
            <option key={computer.id} value={computer.id}>
              {computer.serial_number} · {computer.brand} {computer.model}
            </option>
          ))}
        </select>
      </div>
      <div className="field">
        <label htmlFor="assignment_notes">Observaciones</label>
        <textarea
          id="assignment_notes"
          value={form.notes}
          onChange={(event) =>
            setForm((current) => ({ ...current, notes: event.target.value }))
          }
          placeholder="Comentarios opcionales de entrega"
        />
      </div>
      <button
        className="primary-button"
        disabled={
          saving || availableStudents.length === 0 || availableComputers.length === 0
        }
        type="submit"
      >
        {saving ? 'Asignando...' : 'Asignar computador'}
      </button>
    </form>
  )
}
