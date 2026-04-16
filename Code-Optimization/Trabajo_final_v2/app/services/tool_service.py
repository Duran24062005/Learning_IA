from app.models.records import ToolRecord
from app.services.transform_service import TransformService
from app.services.validation_service import ValidationService


class ToolService:
    def __init__(self, repository, category_service) -> None:
        self.repository = repository
        self.category_service = category_service

    def create(self) -> dict:
        category_id = ValidationService.validar_entero("Ingrese el id de la categoria: ")
        while self.category_service.validate_category(category_id) is False:
            category_id = ValidationService.validar_entero("Error, Categoria no encontrada. Intente nuevamente: ")

        record = ToolRecord(
            id=self.repository.next_id(),
            nombre=ValidationService.validar_texto("Ingrese el nombre: ", 1, 20),
            categoria=self.category_service.validate_category(category_id),
            cantidad=ValidationService.validar_entero("Selecciona la cantidad disponible de esta herramienta: "),
            estado=TransformService.transformar_estado(
                ValidationService.validar_menu(
                    """
                                            Seleccion una de las 3 opciones del estado de una herramienta:
                                            1. Activa
                                            2. Fuera de servicio
                                            3. Reparación
                                            """,
                    1,
                    3,
                )
            ),
            precio=ValidationService.validar_entero("Ingrese el valor que le costo la herramienta: "),
        )
        records = self.repository.load_all()
        records.append(record.to_dict())
        self.repository.save_all(records)
        print("DATOS GUARDADOS CORRECTAMENTE!")
        return record.to_dict()

    def list_all(self) -> list[dict]:
        return self.repository.load_all()

    def find_by_id(self, tool_id: int) -> dict | None:
        for record in self.repository.load_all():
            if record.get("id", "clave no encontrada") == tool_id:
                return record
        return None

    def validate_tool(self, tool_id: int):
        tool = self.find_by_id(tool_id)
        if tool:
            categoria = tool.get("categoria", "clave no encontrada")
            if isinstance(categoria, dict):
                categoria = categoria.get("categoria", "clave no encontrada")
            return {
                "id": tool.get("id", "clave no encontrada"),
                "nombre": tool.get("nombre", "clave no encontrada"),
                "categoria": categoria,
                "estado": tool.get("estado", "clave no encontrada"),
                "precio": tool.get("precio", "clave no encontrada"),
                "cantidad": tool.get("cantidad", "clave no encontrada"),
            }

    def update(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede actualizar porque no hay registros")
            return None
        tool_id = ValidationService.validar_entero("Ingrese el id a actualizar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == tool_id:
                option = ValidationService.validar_menu(
                    """
                                    1. Nombre.
                                    2. Categoria.
                                    3. Estado.
                                    4. Precio
                                    5. Cantidad
                                    6. Cancelar
                                        """,
                    1,
                    6,
                )
                match option:
                    case 1:
                        record["nombre"] = ValidationService.validar_texto("Ingrese el nombre: ", 1, 20)
                    case 2:
                        category_id = ValidationService.validar_entero("Ingrese el id de la categoria: ")
                        while self.category_service.validate_category(category_id) is False:
                            category_id = ValidationService.validar_entero(
                                "Error, categoria no encontrada. Intente nuevamente: "
                            )
                        record["categoria"] = self.category_service.validate_category(category_id)
                    case 3:
                        record["estado"] = TransformService.transformar_estado(
                            ValidationService.validar_menu(
                                """
                                        Seleccion una de las 3 opciones del estado de una herramienta:
                                        1. Activa
                                        2. Fuera de servicio
                                        3. Reparación
                                        """,
                                1,
                                3,
                            )
                        )
                    case 4:
                        record["precio"] = ValidationService.validar_entero(
                            "Ingrese el valor que le costo la herramienta: "
                        )
                    case 5:
                        record["cantidad"] = ValidationService.validar_entero(
                            "Selecciona la cantidad disponible de esta herramienta: "
                        )
                    case 6:
                        print("Operación cancelada!")
                self.repository.save_all(records)
                print("DATO ACTUALIZADO!")
                return record
        print("NO SE ENCONTRÓ EL ID: ", tool_id)
        return None

    def delete(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede actualizar porque no hay registros")
            return None
        tool_id = ValidationService.validar_entero("Ingrese el id a eliminar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == tool_id:
                print(f"""{record.get('nombre', 'clave no encontrada')} ya no esta entre nosotros!""")
                records.remove(record)
                self.repository.save_all(records)
                return record
        print("NO SE ENCONTRÓ EL ID: ", tool_id)
        return None

    def decrease_stock(self, tool_id: int, loan_quantity: int) -> dict | None:
        records = self.repository.load_all()
        for record in records:
            if record.get("id", "Clave no encontrada") == tool_id:
                if record.get("cantidad") >= loan_quantity:
                    record["cantidad"] = record.get("cantidad", "Clave no encontrada") - loan_quantity
                    self.repository.save_all(records)
                    return record
        return None
