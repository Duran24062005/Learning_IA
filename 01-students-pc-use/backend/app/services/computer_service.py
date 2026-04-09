from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.assignment import Assignment
from app.models.computer import Computer
from app.models.computer import ComputerStatus
from app.schemas.computer import ComputerCreate, ComputerUpdate


class ComputerService:
    def create(self, db: Session, payload: ComputerCreate) -> Computer:
        self._ensure_unique_serial(db, payload.serial_number)
        if payload.status == ComputerStatus.ASSIGNED:
            raise ConflictError("Assigned status is reserved for active assignments.")
        computer = Computer(**payload.model_dump())
        db.add(computer)
        db.commit()
        db.refresh(computer)
        return computer

    def list(self, db: Session, *, available_only: bool = False) -> list[Computer]:
        query = select(Computer).order_by(Computer.created_at.desc())
        if available_only:
            query = query.where(Computer.status == "available")
        return list(db.scalars(query))

    def get(self, db: Session, computer_id: str) -> Computer:
        computer = db.get(Computer, computer_id)
        if not computer:
            raise NotFoundError("Computer not found.")
        return computer

    def update(self, db: Session, computer_id: str, payload: ComputerUpdate) -> Computer:
        computer = self.get(db, computer_id)
        updates = payload.model_dump(exclude_unset=True)
        active_assignment = db.scalar(
            select(Assignment).where(
                Assignment.computer_id == computer.id,
                Assignment.returned_at.is_(None),
            )
        )

        serial_number = updates.get("serial_number")
        if serial_number and serial_number != computer.serial_number:
            existing = db.scalar(select(Computer).where(Computer.serial_number == serial_number))
            if existing:
                raise ConflictError("Serial number is already registered.")
        status = updates.get("status")
        if status == ComputerStatus.ASSIGNED:
            raise ConflictError("Assigned status is reserved for active assignments.")
        if active_assignment and status in {ComputerStatus.AVAILABLE, ComputerStatus.MAINTENANCE}:
            raise ConflictError("Cannot manually change the status of a computer with an active assignment.")

        for field, value in updates.items():
            setattr(computer, field, value)

        db.commit()
        db.refresh(computer)
        return computer

    def _ensure_unique_serial(self, db: Session, serial_number: str) -> None:
        if db.scalar(select(Computer).where(Computer.serial_number == serial_number)):
            raise ConflictError("Serial number is already registered.")


computer_service = ComputerService()
