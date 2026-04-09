import { useState } from 'react'
import { ComputerForm } from '../components/computers/ComputerForm'
import { ComputersTable } from '../components/computers/ComputersTable'
import { ErrorMessage } from '../components/common/ErrorMessage'
import { useComputers } from '../hooks/useComputers'
import { getApiErrorMessage } from '../utils/errorHandler'
import type { Computer } from '../types'

export function ComputersPage() {
  const { computers, loading, createComputer, updateComputer } = useComputers()
  const [pageError, setPageError] = useState<string | null>(null)

  const markAvailable = async (computer: Computer) => {
    try {
      setPageError(null)
      await updateComputer(computer.id, { status: 'available' })
    } catch (error) {
      setPageError(getApiErrorMessage(error))
    }
  }

  const markMaintenance = async (computer: Computer) => {
    try {
      setPageError(null)
      await updateComputer(computer.id, { status: 'maintenance' })
    } catch (error) {
      setPageError(getApiErrorMessage(error))
    }
  }

  return (
    <section className="page-grid">
      <div className="page-header">
        <h2>Computadores</h2>
        <p>
          Lleva el inventario actualizado, identifica disponibilidad inmediata y marca
          equipos en mantenimiento sin salir del flujo principal.
        </p>
      </div>
      <div className="two-column">
        <article className="panel">
          <h3>Nuevo computador</h3>
          <ComputerForm onSubmit={createComputer} />
        </article>
        <article className="panel">
          <div className="meta-list">
            <span className="meta-chip">Total: {computers.length}</span>
            <span className="meta-chip">
              Disponibles: {computers.filter((computer) => computer.status === 'available').length}
            </span>
          </div>
          <ErrorMessage message={pageError} />
          {loading ? (
            <div className="empty-state">Cargando computadores...</div>
          ) : (
            <ComputersTable
              computers={computers}
              onSetAvailable={markAvailable}
              onSetMaintenance={markMaintenance}
            />
          )}
        </article>
      </div>
    </section>
  )
}
