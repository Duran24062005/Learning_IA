import tempfile
import unittest
from pathlib import Path

from app.persistence.file_repositories import JsonFileRepository, TextLogRepository
from app.services.report_service import ReportService
from app.services.trace_service import TraceService


class ReportServiceTestCase(unittest.TestCase):
    def test_stock_minimo_keeps_first_match_behavior(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            tools = JsonFileRepository(Path(temp_dir) / "herramientas.json")
            loans = JsonFileRepository(Path(temp_dir) / "prestamos.json")
            users = JsonFileRepository(Path(temp_dir) / "usuarios.json")

            tools.save_all(
                [
                    {"id": 1, "nombre": "Taladro", "cantidad": 2, "categoria": {}},
                    {"id": 2, "nombre": "Martillo", "cantidad": 1, "categoria": {}},
                ]
            )

            service = ReportService(tools, loans, users)

            result = service.stock_minimo(3)

            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["id"], 1)


class TraceServiceTestCase(unittest.TestCase):
    def test_log_message_contains_context(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_repository = TextLogRepository(Path(temp_dir) / "historial.txt")
            trace = TraceService(log_repository)

            message = trace.log("usuario", "crear", "registro generado", echo=False)

            self.assertIn("[usuario.crear]", message)
            self.assertIn("registro generado", message)


if __name__ == "__main__":
    unittest.main()
