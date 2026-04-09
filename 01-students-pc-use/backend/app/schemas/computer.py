from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.computer import ComputerStatus


class ComputerBase(BaseModel):
    serial_number: str
    brand: str
    model: str


class ComputerCreate(ComputerBase):
    status: ComputerStatus = ComputerStatus.AVAILABLE


class ComputerUpdate(BaseModel):
    serial_number: str | None = None
    brand: str | None = None
    model: str | None = None
    status: ComputerStatus | None = None


class ComputerOut(ComputerBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    status: ComputerStatus
    created_at: datetime
