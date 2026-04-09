import pytest

from app.core.exceptions import ConflictError
from app.schemas.student import StudentCreate
from app.services.student_service import student_service


def test_create_student(db):
    student = student_service.create(
        db,
        StudentCreate(
            full_name="Ana Torres",
            document_id="123",
            email="ana@example.com",
            is_active=True,
        ),
    )

    assert student.full_name == "Ana Torres"
    assert student.document_id == "123"


def test_reject_duplicate_student_email(db):
    payload = StudentCreate(
        full_name="Ana Torres",
        document_id="123",
        email="ana@example.com",
        is_active=True,
    )
    student_service.create(db, payload)

    with pytest.raises(ConflictError, match="Email is already registered."):
        student_service.create(
            db,
            StudentCreate(
                full_name="Pedro Rojas",
                document_id="456",
                email="ana@example.com",
                is_active=True,
            ),
        )
