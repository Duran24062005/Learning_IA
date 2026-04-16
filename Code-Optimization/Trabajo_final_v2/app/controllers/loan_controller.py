from app.services.validation_service import ValidationService
from app.views.display import print_loans, print_tools, print_users
from app.views.menus import LOAN_ADMIN_MENU, LOAN_RESIDENT_MENU


class LoanAdminController:
    def __init__(self, loan_service, trace_service) -> None:
        self.loan_service = loan_service
        self.trace_service = trace_service

    def run(self) -> None:
        while True:
            option = ValidationService.validar_menu(LOAN_ADMIN_MENU, 1, 5)
            match option:
                case 1:
                    self._list_all()
                    self.loan_service.manage()
                    self.trace_service.log("prestamo", "gestionar", "Se ha gestionado una solicitud de prestamo")
                case 2:
                    loan = self.loan_service.search()
                    if loan:
                        print_loans([loan])
                case 3:
                    self._list_all()
                case 4:
                    self._list_all()
                    self.loan_service.delete()
                    self.trace_service.log("prestamo", "eliminar", "Se ha eliminado una solicitod de prestamo")
                case 5:
                    break

    def _list_all(self) -> None:
        print_loans(self.loan_service.list_all())


class LoanResidentController:
    def __init__(self, loan_service) -> None:
        self.loan_service = loan_service

    def run(self, user_service, tool_service) -> None:
        while True:
            option = ValidationService.validar_menu(LOAN_RESIDENT_MENU, 1, 3)
            match option:
                case 1:
                    print_users(user_service.list_all())
                    print_tools(tool_service.list_all())
                    self.loan_service.create()
                case 2:
                    print_loans(self.loan_service.consult_by_user())
                case 3:
                    break
