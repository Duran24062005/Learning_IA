from app.models.records import CategoryRecord
from app.services.validation_service import ValidationService


class CategoryService:
    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self) -> dict:
        record = CategoryRecord(
            id=self.repository.next_id(),
            nombre=ValidationService.validar_texto("Ingrese la categoria de la herramienta: ", 1, 30),
        )
        records = self.repository.load_all()
        records.append(record.to_dict())
        self.repository.save_all(records)
        return record.to_dict()

    def list_all(self) -> list[dict]:
        return self.repository.load_all()

    def find_by_id(self, category_id: int) -> dict | None:
        for record in self.repository.load_all():
            if record.get("id", "clave no encontrada") == category_id:
                return record
        return None

    def validate_category(self, category_id: int):
        category = self.find_by_id(category_id)
        if category:
            return {"id": category.get("id"), "categoria": category.get("nombre")}
        return False

    def update(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede actualizar porque no hay registros")
            return None
        category_id = ValidationService.validar_entero("Ingrese el id a actualizar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == category_id:
                option = ValidationService.validar_menu(
                    """
                                    1. Nombre Categoria.
                                    2. Cancelar
                                        """,
                    1,
                    2,
                )
                match option:
                    case 1:
                        record["nombre"] = ValidationService.validar_texto("Ingrese la categoria: ", 1, 20)
                    case 2:
                        print("Operación cancelada!")
                self.repository.save_all(records)
                print("DATO ACTUALIZADO!")
                return record
        print("NO SE ENCONTRÓ EL ID: ", category_id)
        return None

    def delete(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede eliminar porque no hay registros")
            return None
        category_id = ValidationService.validar_entero("Ingrese el id a eliminar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == category_id:
                print(f"""{record.get('categoria', 'clave no encontrada')} ya no esta entre nosotros!""")
                records.remove(record)
                self.repository.save_all(records)
                return record
        print("NO SE ENCONTRÓ EL ID: ", category_id)
        return None
