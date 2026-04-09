from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class StudentBase(BaseModel):
    full_name: str
    document_id: str
    email: EmailStr


class StudentCreate(StudentBase):
    is_active: bool = True


class StudentUpdate(BaseModel):
    full_name: str | None = None
    document_id: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None


class StudentOut(StudentBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    is_active: bool
    created_at: datetime
