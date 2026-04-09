import type { ComputerStatus } from '../../types'

interface StatusBadgeProps {
  status: ComputerStatus
}

const labels: Record<ComputerStatus, string> = {
  available: 'Disponible',
  assigned: 'Asignado',
  maintenance: 'Mantenimiento',
}

export function StatusBadge({ status }: StatusBadgeProps) {
  return <span className={`status-badge ${status}`}>{labels[status]}</span>
}
