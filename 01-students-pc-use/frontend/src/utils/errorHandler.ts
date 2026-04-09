export function getApiErrorMessage(error: unknown): string {
  if (error instanceof Error && error.message) {
    return error.message
  }
  return 'No fue posible completar la operación.'
}
