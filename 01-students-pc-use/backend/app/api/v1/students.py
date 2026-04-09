from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.student import StudentCreate, StudentOut, StudentUpdate
from app.services.student_service import student_service

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", response_model=StudentOut, status_code=201)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)) -> StudentOut:
    return student_service.create(db, payload)


@router.get("", response_model=list[StudentOut])
def list_students(
    active_only: bool = Query(default=False),
    db: Session = Depends(get_db),
) -> list[StudentOut]:
    return student_service.list(db, active_only=active_only)


@router.patch("/{student_id}", response_model=StudentOut)
def update_student(
    student_id: str,
    payload: StudentUpdate,
    db: Session = Depends(get_db),
) -> StudentOut:
    return student_service.update(db, student_id, payload)
