export function formatDate(value: string | null): string {
  if (!value) {
    return 'Sin registrar'
  }

  return new Intl.DateTimeFormat('es-CO', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(new Date(value))
}
