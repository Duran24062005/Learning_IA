import { http } from './http'
import type { Computer, ComputerPayload } from '../types'

export const computersApi = {
  list: (availableOnly = false) =>
    http.get<Computer[]>(`/computers${availableOnly ? '?available_only=true' : ''}`),
  create: (payload: ComputerPayload) => http.post<Computer>('/computers', payload),
  update: (computerId: string, payload: Partial<ComputerPayload>) =>
    http.patch<Computer>(`/computers/${computerId}`, payload),
}
