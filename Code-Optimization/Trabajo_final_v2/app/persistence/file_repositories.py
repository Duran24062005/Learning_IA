import json
from pathlib import Path


class JsonFileRepository:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def load_all(self) -> list[dict]:
        try:
            if self.file_path.exists():
                with self.file_path.open("r", encoding="utf-8") as handle:
                    return json.load(handle)
            return []
        except json.JSONDecodeError as error:
            print(error)
            return []

    def save_all(self, records: list[dict]) -> None:
        with self.file_path.open("w", encoding="utf-8") as handle:
            json.dump(records, handle, indent=4, ensure_ascii=False)

    def next_id(self) -> int:
        records = self.load_all()
        if not records:
            return 1
        return records[-1].get("id", "error, id no encontrado") + 1


class TextLogRepository:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, message: str) -> None:
        with self.file_path.open("a", encoding="utf-8") as handle:
            handle.write(message + "\n")
