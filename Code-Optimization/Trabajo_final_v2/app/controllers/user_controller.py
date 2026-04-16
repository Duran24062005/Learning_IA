from app.services.validation_service import ValidationService
from app.views.display import print_users
from app.views.menus import USER_MENU


class UserController:
    def __init__(self, user_service, trace_service) -> None:
        self.user_service = user_service
        self.trace_service = trace_service

    def run(self) -> None:
        while True:
            option = ValidationService.validar_menu(USER_MENU, 1, 6)
            match option:
                case 1:
                    self.user_service.create()
                    self.trace_service.log("usuario", "crear", "Se ha creado un nuevo usuario")
                case 2:
                    self._list_all()
                    self.user_service.update()
                    self.trace_service.log("usuario", "actualizar", "Se ha actualizado un usuario")
                case 3:
                    self._list_all()
                case 4:
                    user = self._search()
                    if user:
                        print_users([user])
                case 5:
                    self._list_all()
                    self.user_service.delete()
                    self.trace_service.log("usuario", "eliminar", "Se ha eliminado un usuario")
                case 6:
                    break

    def _list_all(self) -> None:
        print_users(self.user_service.list_all())

    def _search(self):
        user_id = ValidationService.validar_entero("Ingrese el id a buscar: ")
        user = self.user_service.find_by_id(user_id)
        if not user:
            print("NO SE ENCONTRÓ EL ID: ", user_id)
        return user
