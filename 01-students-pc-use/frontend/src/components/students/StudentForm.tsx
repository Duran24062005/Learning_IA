import { useState, type FormEvent } from 'react'
import { ErrorMessage } from '../common/ErrorMessage'
import type { StudentPayload } from '../../types'
import { getApiErrorMessage } from '../../utils/errorHandler'

interface StudentFormProps {
  onSubmit: (payload: StudentPayload) => Promise<void>
}

const initialForm: StudentPayload = {
  full_name: '',
  document_id: '',
  email: '',
  is_active: true,
}

export function StudentForm({ onSubmit }: StudentFormProps) {
  const [form, setForm] = useState<StudentPayload>(initialForm)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleChange = <K extends keyof StudentPayload>(key: K, value: StudentPayload[K]) => {
    setForm((current) => ({ ...current, [key]: value }))
  }

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
        <label htmlFor="full_name">Nombre completo</label>
        <input
          id="full_name"
          value={form.full_name}
          onChange={(event) => handleChange('full_name', event.target.value)}
          placeholder="Ej. Laura Martínez"
          required
        />
      </div>
      <div className="field">
        <label htmlFor="document_id">Documento</label>
        <input
          id="document_id"
          value={form.document_id}
          onChange={(event) => handleChange('document_id', event.target.value)}
          placeholder="Ej. 1098765432"
          required
        />
      </div>
      <div className="field">
        <label htmlFor="email">Correo</label>
        <input
          id="email"
          type="email"
          value={form.email}
          onChange={(event) => handleChange('email', event.target.value)}
          placeholder="nombre@campuslands.com"
          required
        />
      </div>
      <div className="field">
        <label htmlFor="is_active">Estado</label>
        <select
          id="is_active"
          value={String(form.is_active)}
          onChange={(event) => handleChange('is_active', event.target.value === 'true')}
        >
          <option value="true">Activo</option>
          <option value="false">Inactivo</option>
        </select>
      </div>
      <button className="primary-button" disabled={saving} type="submit">
        {saving ? 'Guardando...' : 'Registrar estudiante'}
      </button>
    </form>
  )
}
