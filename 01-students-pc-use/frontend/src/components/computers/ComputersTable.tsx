import { StatusBadge } from '../common/StatusBadge'
import type { Computer } from '../../types'
import { formatDate } from '../../utils/formatDate'

interface ComputersTableProps {
  computers: Computer[]
  onSetMaintenance: (computer: Computer) => Promise<void>
  onSetAvailable: (computer: Computer) => Promise<void>
}

export function ComputersTable({
  computers,
  onSetMaintenance,
  onSetAvailable,
}: ComputersTableProps) {
  if (computers.length === 0) {
    return <div className="empty-state">Aún no hay computadores registrados.</div>
  }

  return (
    <div className="table-wrap">
      <table className="data-table">
        <thead>
          <tr>
            <th>Serial</th>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Estado</th>
            <th>Registro</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {computers.map((computer) => (
            <tr key={computer.id}>
              <td>{computer.serial_number}</td>
              <td>{computer.brand}</td>
              <td>{computer.model}</td>
              <td>
                <StatusBadge status={computer.status} />
              </td>
              <td>{formatDate(computer.created_at)}</td>
              <td>
                <div className="button-row">
                  <button
                    className="secondary-button"
                    disabled={computer.status === 'assigned'}
                    onClick={() => void onSetAvailable(computer)}
                    type="button"
                  >
                    Marcar disponible
                  </button>
                  <button
                    className="secondary-button"
                    disabled={computer.status === 'assigned'}
                    onClick={() => void onSetMaintenance(computer)}
                    type="button"
                  >
                    Mantenimiento
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
