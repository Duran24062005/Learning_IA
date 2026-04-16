from app.services.validation_service import ValidationService
from app.views.display import print_lines, print_loans, print_tools
from app.views.menus import REPORT_MENU


class ReportController:
    def __init__(self, report_service) -> None:
        self.report_service = report_service

    def run(self) -> None:
        while True:
            option = ValidationService.validar_menu(REPORT_MENU, 1, 6)
            match option:
                case 1:
                    stock = ValidationService.validar_entero(
                        "Ingrese la cantidad stock minimo que se encuentre disponible en las herramientas que desea buscar: "
                    )
                    print_tools(self.report_service.stock_minimo(stock))
                case 2:
                    estado = ValidationService.validar_menu(
                        """
                        1. En proceso
                        2. Completados
                        """,
                        1,
                        2,
                    )
                    print_loans(self.report_service.prestamos_por_estado(estado))
                case 3:
                    user_id = ValidationService.validar_entero(
                        "Ingrese el id de su Usuario. Si no lo conoce contacte al administrador: "
                    )
                    print_loans(self.report_service.historial_usuario(user_id))
                case 4:
                    print_lines(self.report_service.herramienta_mas_usada())
                case 5:
                    print_lines(self.report_service.usuario_mas_usado())
                case 6:
                    break
