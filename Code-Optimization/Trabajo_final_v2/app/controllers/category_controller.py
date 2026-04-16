from app.services.validation_service import ValidationService
from app.views.display import print_categories
from app.views.menus import CATEGORY_MENU


class CategoryController:
    def __init__(self, category_service, trace_service) -> None:
        self.category_service = category_service
        self.trace_service = trace_service

    def run(self) -> None:
        while True:
            option = ValidationService.validar_menu(CATEGORY_MENU, 1, 6)
            match option:
                case 1:
                    self.category_service.create()
                    self.trace_service.log("categoria", "crear", "Se ha creado una nueva categoria")
                case 2:
                    self._list_all()
                    self.category_service.update()
                    self.trace_service.log("categoria", "actualizar", "Se ha actualizado una categoria")
                case 3:
                    self._list_all()
                case 4:
                    category = self._search()
                    if category:
                        print_categories([category])
                case 5:
                    self._list_all()
                    self.category_service.delete()
                    self.trace_service.log("categoria", "eliminar", "Se ha eliminado una categoria")
                case 6:
                    break

    def _list_all(self) -> None:
        print_categories(self.category_service.list_all())

    def _search(self):
        category_id = ValidationService.validar_entero("Ingrese el id a buscar: ")
        category = self.category_service.find_by_id(category_id)
        if not category:
            print("NO SE ENCONTRÓ EL ID: ", category_id)
        return category
