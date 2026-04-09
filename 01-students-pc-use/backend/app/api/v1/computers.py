from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.computer import ComputerCreate, ComputerOut, ComputerUpdate
from app.services.computer_service import computer_service

router = APIRouter(prefix="/computers", tags=["computers"])


@router.post("", response_model=ComputerOut, status_code=201)
def create_computer(payload: ComputerCreate, db: Session = Depends(get_db)) -> ComputerOut:
    return computer_service.create(db, payload)


@router.get("", response_model=list[ComputerOut])
def list_computers(
    available_only: bool = Query(default=False),
    db: Session = Depends(get_db),
) -> list[ComputerOut]:
    return computer_service.list(db, available_only=available_only)


@router.patch("/{computer_id}", response_model=ComputerOut)
def update_computer(
    computer_id: str,
    payload: ComputerUpdate,
    db: Session = Depends(get_db),
) -> ComputerOut:
    return computer_service.update(db, computer_id, payload)
