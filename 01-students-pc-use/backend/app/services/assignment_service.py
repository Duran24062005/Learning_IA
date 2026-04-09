from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.core.exceptions import ConflictError, NotFoundError
from app.models.assignment import Assignment
from app.models.computer import ComputerStatus
from app.schemas.assignment import AssignmentCreate, AssignmentReturn
from app.services.computer_service import computer_service
from app.services.student_service import student_service


class AssignmentService:
    def create(self, db: Session, payload: AssignmentCreate) -> Assignment:
        student = student_service.get(db, payload.student_id)
        computer = computer_service.get(db, payload.computer_id)

        if not student.is_active:
            raise ConflictError("Inactive students cannot receive a computer.")
        if computer.status != ComputerStatus.AVAILABLE:
            raise ConflictError("Only available computers can be assigned.")

        active_assignment = db.scalar(
            select(Assignment).where(
                Assignment.computer_id == computer.id,
                Assignment.returned_at.is_(None),
            )
        )
        if active_assignment:
            raise ConflictError("This computer already has an active assignment.")

        assignment = Assignment(**payload.model_dump())
        computer.status = ComputerStatus.ASSIGNED
        db.add(assignment)
        db.commit()
        return self.get(db, assignment.id)

    def list(
        self,
        db: Session,
        *,
        student_id: str | None = None,
        computer_id: str | None = None,
        active_only: bool = False,
    ) -> list[Assignment]:
        query = (
            select(Assignment)
            .options(joinedload(Assignment.student), joinedload(Assignment.computer))
            .order_by(Assignment.assigned_at.desc())
        )
        if student_id:
            query = query.where(Assignment.student_id == student_id)
        if computer_id:
            query = query.where(Assignment.computer_id == computer_id)
        if active_only:
            query = query.where(Assignment.returned_at.is_(None))

        return list(db.scalars(query).unique())

    def get(self, db: Session, assignment_id: str) -> Assignment:
        assignment = db.scalar(
            select(Assignment)
            .options(joinedload(Assignment.student), joinedload(Assignment.computer))
            .where(Assignment.id == assignment_id)
        )
        if not assignment:
            raise NotFoundError("Assignment not found.")
        return assignment

    def return_assignment(
        self,
        db: Session,
        assignment_id: str,
        payload: AssignmentReturn,
    ) -> Assignment:
        assignment = db.scalar(select(Assignment).where(Assignment.id == assignment_id))
        if not assignment:
            raise NotFoundError("Assignment not found.")
        if assignment.returned_at is not None:
            raise ConflictError("This assignment was already returned.")

        computer = computer_service.get(db, assignment.computer_id)
        assignment.returned_at = datetime.now(timezone.utc)
        if payload.notes:
            assignment.notes = payload.notes
        computer.status = ComputerStatus.AVAILABLE

        db.commit()
        return self.get(db, assignment.id)


assignment_service = AssignmentService()
