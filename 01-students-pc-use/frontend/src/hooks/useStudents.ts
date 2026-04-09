import { useEffect, useState } from 'react'
import { studentsApi } from '../api/studentsApi'
import type { Student, StudentPayload } from '../types'

export function useStudents() {
  const [students, setStudents] = useState<Student[]>([])
  const [loading, setLoading] = useState(true)

  const refreshStudents = async () => {
    setLoading(true)
    try {
      const data = await studentsApi.list()
      setStudents(data)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    void refreshStudents()
  }, [])

  const createStudent = async (payload: StudentPayload) => {
    await studentsApi.create(payload)
    await refreshStudents()
  }

  const updateStudent = async (studentId: string, payload: Partial<StudentPayload>) => {
    await studentsApi.update(studentId, payload)
    await refreshStudents()
  }

  return { students, loading, refreshStudents, createStudent, updateStudent }
}
