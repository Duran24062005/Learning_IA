import { useState, type FormEvent } from 'react'
import { ErrorMessage } from '../common/ErrorMessage'
import type { ComputerPayload } from '../../types'
import { getApiErrorMessage } from '../../utils/errorHandler'

interface ComputerFormProps {
  onSubmit: (payload: ComputerPayload) => Promise<void>
}

const initialForm: ComputerPayload = {
  serial_number: '',
  brand: '',
  model: '',
  status: 'available',
}

export function ComputerForm({ onSubmit }: ComputerFormProps) {
  const [form, setForm] = useState<ComputerPayload>(initialForm)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleChange = <K extends keyof ComputerPayload>(key: K, value: ComputerPayload[K]) => {
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
        <label htmlFor="serial_number">Serial</label>
        <input
          id="serial_number"
          value={form.serial_number}
          onChange={(event) => handleChange('serial_number', event.target.value)}
          placeholder="Ej. CJS-001"
          required
        />
      </div>
      <div className="field">
        <label htmlFor="brand">Marca</label>
        <input
          id="brand"
          value={form.brand}
          onChange={(event) => handleChange('brand', event.target.value)}
          placeholder="Dell, Lenovo, HP..."
          required
        />
      </div>
      <div className="field">
        <label htmlFor="model">Modelo</label>
        <input
          id="model"
          value={form.model}
          onChange={(event) => handleChange('model', event.target.value)}
          placeholder="Latitude 5420"
          required
        />
      </div>
      <div className="field">
        <label htmlFor="status">Estado inicial</label>
        <select
          id="status"
          value={form.status}
          onChange={(event) => handleChange('status', event.target.value as ComputerPayload['status'])}
        >
          <option value="available">Disponible</option>
          <option value="maintenance">Mantenimiento</option>
        </select>
      </div>
      <button className="primary-button" disabled={saving} type="submit">
        {saving ? 'Guardando...' : 'Registrar computador'}
      </button>
    </form>
  )
}
