from dataclasses import dataclass
from pathlib import Path

from app.persistence.file_repositories import JsonFileRepository, TextLogRepository


@dataclass
class AppContext:
    category_repository: JsonFileRepository
    user_repository: JsonFileRepository
    tool_repository: JsonFileRepository
    loan_repository: JsonFileRepository
    log_repository: TextLogRepository

    @classmethod
    def build(cls) -> "AppContext":
        base_dir = Path(__file__).resolve().parent.parent.parent
        data_dir = base_dir / "data"
        return cls(
            category_repository=JsonFileRepository(data_dir / "categorias.json"),
            user_repository=JsonFileRepository(data_dir / "usuarios.json"),
            tool_repository=JsonFileRepository(data_dir / "herramientas.json"),
            loan_repository=JsonFileRepository(data_dir / "prestamos.json"),
            log_repository=TextLogRepository(data_dir / "historial.txt"),
        )
