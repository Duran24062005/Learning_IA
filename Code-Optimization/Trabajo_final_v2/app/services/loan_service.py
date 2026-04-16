from datetime import timedelta

from app.models.records import LoanRecord
from app.services.transform_service import TransformService
from app.services.validation_service import ValidationService


class LoanService:
    def __init__(self, repository, tool_service, user_service, trace_service) -> None:
        self.repository = repository
        self.tool_service = tool_service
        self.user_service = user_service
        self.trace_service = trace_service

    def create(self) -> dict:
        records = self.repository.load_all()
        user_id = ValidationService.validar_entero("Ingrese el id del usuario: ")
        while self.user_service.validate_user(user_id) is False:
            user_id = ValidationService.validar_entero("Error, usuario no encontrada. Intente nuevamente: ")

        tool_id = ValidationService.validar_entero("Ingrese el id de la herramienta: ")
        while self.tool_service.validate_tool(tool_id) is False:
            tool_id = ValidationService.validar_entero("Error, Herramienta no enctrada. Intente nuevamente: ")

        start_date = TransformService.solicitar_fecha_inicio()
        dias = ValidationService.validar_entero("Ingrese la cantidad de días a usar la herramienta: ")
        record = LoanRecord(
            id=self.repository.next_id(),
            usuario=self.user_service.validate_user(user_id),
            herramienta=self.tool_service.validate_tool(tool_id),
            cantidad=ValidationService.validar_entero("Ingrese la cantidad de herramientas a solicitar: "),
            fecha_inicio=str(start_date),
            fecha_final=str(start_date + timedelta(days=dias)),
            estado="En proceso",
            observaciones="Pendiente",
        )
        records.append(record.to_dict())
        self.repository.save_all(records)
        print("DATOS GUARDADOS CORRECTAMENTE!")
        print(f"SU ID ES {record.id}, POR FAVOR GUARDELO PARA HACER SEGUIMIENTO")
        return record.to_dict()

    def list_all(self) -> list[dict]:
        return self.repository.load_all()

    def consult_by_user(self) -> list[dict]:
        records = self.repository.load_all()
        results = []
        if not records:
            print("No hay registros en este momento")
            return results
        user_id = ValidationService.validar_entero(
            "Ingrese el id de su Usuario. Si no lo conoce contacte al administrador: "
        )
        for record in records:
            if record.get("usuario", "Clave no encontrada").get("id", "id no encontrado") == user_id:
                results.append(record)
        return results

    def find_by_id(self, loan_id: int) -> dict | None:
        for record in self.repository.load_all():
            if record.get("id", "clave no encontrada") == loan_id:
                return record
        return None

    def search(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede buscar porque no hay registros")
            return None
        loan_id = ValidationService.validar_entero("Ingrese el id a buscar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == loan_id:
                return record
        print("NO SE ENCONTRÓ EL ID: ", loan_id)
        return None

    def manage(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede gestionar porque no hay registros")
            return None
        loan_id = ValidationService.validar_entero("Ingrese el id del prestamo a gestionar: ")
        for record in records:
            if record.get("id", "Clave no encontrada") == loan_id:
                option = ValidationService.validar_menu(
                    """
                                            Seleccione que opción desea realizar con el prestamo:
                                            1. Gestionar
                                            2. Rechazar
                                            """,
                    1,
                    2,
                )
                match option:
                    case 1:
                        self._approve_or_reject_for_stock(record)
                    case 2:
                        self._reject(record)
                self.repository.save_all(records)
                return record
        print("NO SE ENCONTRÓ EL ID: ", loan_id)
        return None

    def delete(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede eliminar porque no hay registros")
            return None
        loan_id = ValidationService.validar_entero("Ingrese el id a eliminar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == loan_id:
                print(f"""{record.get('nombre', 'clave no encontrada')} ya no esta entre nosotros!""")
                records.remove(record)
                self.repository.save_all(records)
                return record
        print("NO SE ENCONTRÓ EL ID: ", loan_id)
        return None

    def _approve_or_reject_for_stock(self, loan_record: dict) -> None:
        updated_tool = self.tool_service.decrease_stock(
            loan_record.get("herramienta", "clave no encontrado").get("id", "clave no encontrada"),
            loan_record.get("cantidad", "Clave no encontrada"),
        )
        if updated_tool:
            loan_record["estado"] = "Aceptada"
            loan_record["observaciones"] = (
                "Se aprueba la solicitud, NO olivdes devolver la herramienta en su fecha destinada"
            )
            print(
                "Se acepta la solicitud debido a que hay stock de la herramienta, "
                f"y queda un total de {updated_tool.get('cantidad', 'clave no encontrada')} "
                "unidades de esa herramienta en Stock"
            )
            return
        loan_record["estado"] = "Rechazada"
        loan_record["observaciones"] = "Se rechaza por no haber stock disponible"
        print("No se puede gestionar esta solicitud debido a que no hay suficiente Stock")
        self.trace_service.log(
            "prestamo",
            "stock",
            "Se solicito un prestamo de herramienta pero fue rechazado por no haber suficiente stock solicitado",
        )

    def _reject(self, loan_record: dict) -> None:
        loan_record["observaciones"] = ValidationService.validar_texto(
            "Ingrese el motivo por el cual rechaza la solicitud de prestamo: ",
            1,
            100,
        )
        loan_record["estado"] = "Rechazada"
