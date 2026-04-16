from app.services.validation_service import ValidationService
from app.views.menus import (
    EXIT_ADMIN_MESSAGE,
    EXIT_RESIDENT_MESSAGE,
    GENERAL_ADMIN_MENU,
    GENERAL_RESIDENT_MENU,
)


class MenuController:
    def __init__(
        self,
        auth_controller,
        category_controller,
        tool_controller,
        user_controller,
        loan_admin_controller,
        loan_resident_controller,
        report_controller,
        category_service,
        tool_service,
        user_service,
        loan_service,
        trace_service,
    ) -> None:
        self.auth_controller = auth_controller
        self.category_controller = category_controller
        self.tool_controller = tool_controller
        self.user_controller = user_controller
        self.loan_admin_controller = loan_admin_controller
        self.loan_resident_controller = loan_resident_controller
        self.report_controller = report_controller
        self.category_service = category_service
        self.tool_service = tool_service
        self.user_service = user_service
        self.loan_service = loan_service
        self.trace_service = trace_service

    def run(self) -> None:
        session = self.auth_controller.login()
        if not session:
            return
        while True:
            if session.role == "admin":
                option = ValidationService.validar_menu(GENERAL_ADMIN_MENU, 1, 6)
                match option:
                    case 1:
                        if not self.category_service.list_all():
                            print("NO SE PUEDE REALIZAR NINGUNA OPCIÓN HASTA INGRESAR UNA CATEGORIA")
                            self.trace_service.log(
                                "menu_general",
                                "herramientas",
                                "Se intento hacer un registro de Herramienta pero no hay categorias",
                            )
                        else:
                            self.tool_controller.run()
                    case 2:
                        self.category_controller.run()
                    case 3:
                        self.user_controller.run()
                    case 4:
                        if not self.user_service.list_all() or not self.tool_service.list_all():
                            print(
                                "NO SE PUEDE REALIZAR NINGUNA OPCIÓN DE PRESTAMO HASTA TENER REGISTRO DE USUARIOS Y HERRAMIENTAS"
                            )
                            self.trace_service.log(
                                "menu_general",
                                "prestamos",
                                "Se intento hacer una gestion de prestamo pero no hay usuarios o herramientas registradas",
                            )
                        else:
                            self.loan_admin_controller.run()
                    case 5:
                        if not self.loan_service.list_all() or not self.tool_service.list_all():
                            print("NO SE PUEDE REALIZAR CONSULTAS DE REPORTE PORQUE NO HAY REGISTROS")
                            self.trace_service.log(
                                "menu_general",
                                "reportes",
                                "Se intento hacer una consulta de reporte pero no hay registros en estos momentos",
                            )
                        else:
                            self.report_controller.run()
                    case 6:
                        print(EXIT_ADMIN_MESSAGE)
                        break
            else:
                option = ValidationService.validar_menu(GENERAL_RESIDENT_MENU, 1, 2)
                match option:
                    case 1:
                        if not self.user_service.list_all() or not self.tool_service.list_all():
                            print(
                                "No se puede solicitar un prestamo porque no hay registros de herramienta y usuarios"
                            )
                            print("Contacte al administrador para registrar usuarios y herramientas")
                            self.trace_service.log(
                                "menu_general",
                                "prestamo_residente",
                                "Se intento realizar una solicitud de prestamo pero no se pudo porque no hay registros en usuarios y herramientas",
                            )
                        else:
                            self.loan_resident_controller.run(self.user_service, self.tool_service)
                    case 2:
                        print(EXIT_RESIDENT_MESSAGE)
                        break
