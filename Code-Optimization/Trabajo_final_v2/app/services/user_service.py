from app.models.records import UserRecord
from app.services.transform_service import TransformService
from app.services.validation_service import ValidationService


class UserService:
    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self) -> dict:
        record = UserRecord(
            id=self.repository.next_id(),
            nombre=ValidationService.validar_texto("Ingrese el nombre de la persona: ", 1, 30),
            apellido=ValidationService.validar_texto("Ingrese el apellido de la persona: ", 1, 30),
            telefono=ValidationService.validar_entero("Ingrese su numero de telefono: "),
            direccion=ValidationService.validar_texto("Ingrese la dirección de residencia del usuario: ", 1, 50),
            tipo=TransformService.transformar_tipo(
                ValidationService.validar_menu(
                    """
                                            Seleccion el tipo de usuario:
                                            1. Residente
                                            2. Administrador
                                            """,
                    1,
                    2,
                )
            ),
        )
        records = self.repository.load_all()
        records.append(record.to_dict())
        self.repository.save_all(records)
        print("DATOS GUARDADOS CORRECTAMENTE!")
        return record.to_dict()

    def list_all(self) -> list[dict]:
        return self.repository.load_all()

    def find_by_id(self, user_id: int) -> dict | None:
        for record in self.repository.load_all():
            if record.get("id", "clave no encontrada") == user_id:
                return record
        return None

    def validate_user(self, user_id: int):
        user = self.find_by_id(user_id)
        if user:
            return {
                "id": user.get("id", "clave no encontrada"),
                "nombre": user.get("nombre", "clave no encontrada"),
                "apellido": user.get("apellido", "clave no encontrada"),
                "telefono": user.get("telefono", "clave no encontrada"),
                "direccion": user.get("direccion", "clave no encontrada"),
            }

    def update(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede actualizar porque no hay registros")
            return None
        user_id = ValidationService.validar_entero("Ingrese el id a actualizar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == user_id:
                option = ValidationService.validar_menu(
                    """
                                    1. Nombre.
                                    2. Apellido.
                                    3. Telefono.
                                    4. Direccion
                                    5. Tipo de usuario
                                    6. Cancelar
                                        """,
                    1,
                    5,
                )
                match option:
                    case 1:
                        record["nombre"] = ValidationService.validar_texto("Ingrese el nombre: ", 1, 20)
                    case 2:
                        record["apellido"] = ValidationService.validar_texto("Ingrese el nombre: ", 1, 20)
                    case 3:
                        record["telefono"] = ValidationService.validar_entero("Ingrese su numero de telefono: ")
                    case 4:
                        record["direccion"] = ValidationService.validar_texto(
                            "Ingrese la dirección de residencia del usuario: ",
                            1,
                            50,
                        )
                    case 5:
                        record["tipo"] = TransformService.transformar_tipo(
                            ValidationService.validar_menu(
                                """
                                            Seleccion el tipo de usuario:
                                            1. Residente
                                            2. Administrador
                                            """,
                                1,
                                2,
                            )
                        )
                    case 6:
                        print("Operación cancelada!")
                self.repository.save_all(records)
                print("DATO ACTUALIZADO!")
                return record
        print("NO SE ENCONTRÓ EL ID: ", user_id)
        return None

    def delete(self) -> dict | None:
        records = self.repository.load_all()
        if not records:
            print("No se puede actualizar porque no hay registros")
            return None
        user_id = ValidationService.validar_entero("Ingrese el id a eliminar: ")
        for record in records:
            if record.get("id", "clave no encontrada") == user_id:
                print(f"""{record.get('nombre', 'clave no encontrada')} ya no esta entre nosotros!""")
                records.remove(record)
                self.repository.save_all(records)
                return record
        print("NO SE ENCONTRÓ EL ID: ", user_id)
        return None
