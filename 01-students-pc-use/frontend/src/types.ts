export type ComputerStatus = 'available' | 'assigned' | 'maintenance'

export interface Student {
  id: string
  full_name: string
  document_id: string
  email: string
  is_active: boolean
  created_at: string
}

export interface Computer {
  id: string
  serial_number: string
  brand: string
  model: string
  status: ComputerStatus
  created_at: string
}

export interface Assignment {
  id: string
  student_id: string
  computer_id: string
  assigned_at: string
  returned_at: string | null
  notes: string | null
  student: Student
  computer: Computer
}

export interface StudentPayload {
  full_name: string
  document_id: string
  email: string
  is_active: boolean
}

export interface ComputerPayload {
  serial_number: string
  brand: string
  model: string
  status: ComputerStatus
}

export interface AssignmentPayload {
  student_id: string
  computer_id: string
  notes: string
}

export interface AssignmentReturnPayload {
  notes: string
}
