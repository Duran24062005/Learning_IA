import pytest

from app.core.exceptions import ConflictError
from app.schemas.assignment import AssignmentCreate, AssignmentReturn
from app.schemas.computer import ComputerCreate
from app.schemas.student import StudentCreate
from app.services.assignment_service import assignment_service
from app.services.computer_service import computer_service
from app.services.student_service import student_service


def create_student(db, *, active=True, email="ana@example.com", document_id="123"):
    return student_service.create(
        db,
        StudentCreate(
            full_name="Ana Torres",
            document_id=document_id,
            email=email,
            is_active=active,
        ),
    )


def create_computer(db, *, serial="SN-001", status="available"):
    return computer_service.create(
        db,
        ComputerCreate(
            serial_number=serial,
            brand="Dell",
            model="Latitude 5420",
            status=status,
        ),
    )


def test_assign_computer_to_active_student(db):
    student = create_student(db)
    computer = create_computer(db)

    assignment = assignment_service.create(
        db,
        AssignmentCreate(
            student_id=student.id,
            computer_id=computer.id,
            notes="Primera asignacion",
        ),
    )

    assert assignment.returned_at is None
    assert assignment.computer.status.value == "assigned"


def test_reject_assignment_when_computer_unavailable(db):
    student = create_student(db)
    computer = create_computer(db, status="maintenance")

    with pytest.raises(ConflictError, match="Only available computers can be assigned."):
      assignment_service.create(
            db,
            AssignmentCreate(
                student_id=student.id,
                computer_id=computer.id,
                notes=None,
            ),
        )


def test_reject_assignment_to_inactive_student(db):
    student = create_student(
        db,
        active=False,
        email="inactive@example.com",
        document_id="987",
    )
    computer = create_computer(db)

    with pytest.raises(ConflictError, match="Inactive students cannot receive a computer."):
        assignment_service.create(
            db,
            AssignmentCreate(
                student_id=student.id,
                computer_id=computer.id,
                notes=None,
            ),
        )


def test_return_assignment_frees_computer(db):
    student = create_student(db)
    computer = create_computer(db)
    assignment = assignment_service.create(
        db,
        AssignmentCreate(student_id=student.id, computer_id=computer.id, notes=None),
    )

    returned = assignment_service.return_assignment(
        db,
        assignment.id,
        AssignmentReturn(notes="Equipo devuelto"),
    )

    assert returned.returned_at is not None
    assert returned.computer.status.value == "available"


def test_assignment_history_filters(db):
    student = create_student(db)
    computer = create_computer(db)
    assignment = assignment_service.create(
        db,
        AssignmentCreate(student_id=student.id, computer_id=computer.id, notes=None),
    )
    assignment_service.return_assignment(db, assignment.id, AssignmentReturn(notes=None))

    history = assignment_service.list(db, student_id=student.id)

    assert len(history) == 1
    assert history[0].student_id == student.id
