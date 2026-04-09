import pytest

from app.core.exceptions import ConflictError
from app.schemas.computer import ComputerCreate
from app.services.computer_service import computer_service


def test_create_computer(db):
    computer = computer_service.create(
        db,
        ComputerCreate(
            serial_number="SN-001",
            brand="Dell",
            model="Latitude 5420",
            status="available",
        ),
    )

    assert computer.serial_number == "SN-001"


def test_reject_duplicate_serial(db):
    payload = ComputerCreate(
        serial_number="SN-001",
        brand="Dell",
        model="Latitude 5420",
        status="available",
    )
    computer_service.create(db, payload)

    with pytest.raises(ConflictError, match="Serial number is already registered."):
        computer_service.create(db, payload)
