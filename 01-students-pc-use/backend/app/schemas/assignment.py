from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.computer import ComputerOut
from app.schemas.student import StudentOut


class AssignmentCreate(BaseModel):
    student_id: str
    computer_id: str
    notes: str | None = None


class AssignmentReturn(BaseModel):
    notes: str | None = None


class AssignmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    student_id: str
    computer_id: str
    assigned_at: datetime
    returned_at: datetime | None
    notes: str | None
    student: StudentOut
    computer: ComputerOut
