from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


class StudentService:
    def create(self, db: Session, payload: StudentCreate) -> Student:
        self._ensure_unique_fields(db, payload.document_id, payload.email)
        student = Student(**payload.model_dump())
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    def list(self, db: Session, *, active_only: bool = False) -> list[Student]:
        query = select(Student).order_by(Student.created_at.desc())
        if active_only:
            query = query.where(Student.is_active.is_(True))
        return list(db.scalars(query))

    def get(self, db: Session, student_id: str) -> Student:
        student = db.get(Student, student_id)
        if not student:
            raise NotFoundError("Student not found.")
        return student

    def update(self, db: Session, student_id: str, payload: StudentUpdate) -> Student:
        student = self.get(db, student_id)
        updates = payload.model_dump(exclude_unset=True)

        document_id = updates.get("document_id")
        email = updates.get("email")
        if document_id and document_id != student.document_id:
            existing = db.scalar(select(Student).where(Student.document_id == document_id))
            if existing:
                raise ConflictError("Document ID is already registered.")
        if email and email != student.email:
            existing = db.scalar(select(Student).where(Student.email == email))
            if existing:
                raise ConflictError("Email is already registered.")

        for field, value in updates.items():
            setattr(student, field, value)

        db.commit()
        db.refresh(student)
        return student

    def _ensure_unique_fields(self, db: Session, document_id: str, email: str) -> None:
        if db.scalar(select(Student).where(Student.document_id == document_id)):
            raise ConflictError("Document ID is already registered.")
        if db.scalar(select(Student).where(Student.email == email)):
            raise ConflictError("Email is already registered.")


student_service = StudentService()
