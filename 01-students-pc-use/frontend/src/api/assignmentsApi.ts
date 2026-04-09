import { http } from './http'
import type {
  Assignment,
  AssignmentPayload,
  AssignmentReturnPayload,
} from '../types'

export const assignmentsApi = {
  list: (filters?: { studentId?: string; computerId?: string; activeOnly?: boolean }) => {
    const params = new URLSearchParams()
    if (filters?.studentId) params.set('student_id', filters.studentId)
    if (filters?.computerId) params.set('computer_id', filters.computerId)
    if (filters?.activeOnly) params.set('active_only', 'true')
    const query = params.toString()
    return http.get<Assignment[]>(`/assignments${query ? `?${query}` : ''}`)
  },
  create: (payload: AssignmentPayload) => http.post<Assignment>('/assignments', payload),
  returnAssignment: (assignmentId: string, payload: AssignmentReturnPayload) =>
    http.post<Assignment>(`/assignments/${assignmentId}/return`, payload),
}
