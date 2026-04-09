from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.assignment import AssignmentCreate, AssignmentOut, AssignmentReturn
from app.services.assignment_service import assignment_service

router = APIRouter(prefix="/assignments", tags=["assignments"])


@router.post("", response_model=AssignmentOut, status_code=201)
def create_assignment(
    payload: AssignmentCreate,
    db: Session = Depends(get_db),
) -> AssignmentOut:
    return assignment_service.create(db, payload)


@router.post("/{assignment_id}/return", response_model=AssignmentOut)
def return_assignment(
    assignment_id: str,
    payload: AssignmentReturn,
    db: Session = Depends(get_db),
) -> AssignmentOut:
    return assignment_service.return_assignment(db, assignment_id, payload)


@router.get("", response_model=list[AssignmentOut])
def list_assignments(
    student_id: str | None = Query(default=None),
    computer_id: str | None = Query(default=None),
    active_only: bool = Query(default=False),
    db: Session = Depends(get_db),
) -> list[AssignmentOut]:
    return assignment_service.list(
        db,
        student_id=student_id,
        computer_id=computer_id,
        active_only=active_only,
    )
