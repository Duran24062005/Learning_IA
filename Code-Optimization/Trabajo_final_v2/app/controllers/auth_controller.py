from app.models.records import SessionRecord
from app.services.validation_service import ValidationService
from app.views.menus import EXIT_SYSTEM_MESSAGE, LOGIN_MENU


class AuthController:
    def __init__(self, auth_service) -> None:
        self.auth_service = auth_service

    def login(self) -> SessionRecord | None:
        while True:
            option = ValidationService.validar_menu(LOGIN_MENU, 1, 3)
            match option:
                case 1:
                    print("-" * 15)
                    print("[ZONA DE ACCESO RESTRINGIDO: ADMIN]")
                    print("-" * 15)
                    password = input("Introduce la clave de seguridad para continuar: ")
                    role = self.auth_service.login(option, password)
                    if role:
                        return SessionRecord(role=role)
                    print("Contreseña incorrecta, sera regresado al menu de ingreso")
                case 2:
                    print("-" * 15)
                    print("[ ÁREA DE RESIDENTES: MI HOGAR ]")
                    print("-" * 15)
                    password = input("Introduce la clave de seguridad de residente: ")
                    role = self.auth_service.login(option, password)
                    if role:
                        return SessionRecord(role=role)
                    print("Contreseña incorrecta, sera regresado al menu de ingreso")
                case 3:
                    print(EXIT_SYSTEM_MESSAGE)
                    return None
