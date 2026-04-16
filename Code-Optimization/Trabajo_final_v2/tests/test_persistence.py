import tempfile
import unittest
from pathlib import Path

from app.persistence.file_repositories import JsonFileRepository, TextLogRepository


class JsonFileRepositoryTestCase(unittest.TestCase):
    def test_next_id_uses_last_record(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repository = JsonFileRepository(Path(temp_dir) / "usuarios.json")
            repository.save_all([{"id": 1}, {"id": 4}])

            self.assertEqual(repository.next_id(), 5)

    def test_load_all_returns_empty_when_file_does_not_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repository = JsonFileRepository(Path(temp_dir) / "faltante.json")

            self.assertEqual(repository.load_all(), [])


class TextLogRepositoryTestCase(unittest.TestCase):
    def test_append_persists_line(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = Path(temp_dir) / "historial.txt"
            repository = TextLogRepository(log_path)

            repository.append("evento de prueba")

            self.assertIn("evento de prueba", log_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
