import { http } from './http'
import type { Student, StudentPayload } from '../types'

export const studentsApi = {
  list: (activeOnly = false) =>
    http.get<Student[]>(`/students${activeOnly ? '?active_only=true' : ''}`),
  create: (payload: StudentPayload) => http.post<Student>('/students', payload),
  update: (studentId: string, payload: Partial<StudentPayload>) =>
    http.patch<Student>(`/students/${studentId}`, payload),
}
