import { useEffect, useState } from 'react'
import { assignmentsApi } from '../api/assignmentsApi'
import type {
  Assignment,
  AssignmentPayload,
  AssignmentReturnPayload,
} from '../types'

export function useAssignments() {
  const [assignments, setAssignments] = useState<Assignment[]>([])
  const [loading, setLoading] = useState(true)

  const refreshAssignments = async () => {
    setLoading(true)
    try {
      const data = await assignmentsApi.list()
      setAssignments(data)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    void refreshAssignments()
  }, [])

  const createAssignment = async (payload: AssignmentPayload) => {
    await assignmentsApi.create(payload)
    await refreshAssignments()
  }

  const returnAssignment = async (assignmentId: string, payload: AssignmentReturnPayload) => {
    await assignmentsApi.returnAssignment(assignmentId, payload)
    await refreshAssignments()
  }

  return { assignments, loading, refreshAssignments, createAssignment, returnAssignment }
}
