import { useEffect, useState } from 'react'
import { computersApi } from '../api/computersApi'
import type { Computer, ComputerPayload } from '../types'

export function useComputers() {
  const [computers, setComputers] = useState<Computer[]>([])
  const [loading, setLoading] = useState(true)

  const refreshComputers = async () => {
    setLoading(true)
    try {
      const data = await computersApi.list()
      setComputers(data)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    void refreshComputers()
  }, [])

  const createComputer = async (payload: ComputerPayload) => {
    await computersApi.create(payload)
    await refreshComputers()
  }

  const updateComputer = async (computerId: string, payload: Partial<ComputerPayload>) => {
    await computersApi.update(computerId, payload)
    await refreshComputers()
  }

  return { computers, loading, refreshComputers, createComputer, updateComputer }
}
