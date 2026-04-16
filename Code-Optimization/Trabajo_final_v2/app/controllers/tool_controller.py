from app.services.validation_service import ValidationService
from app.views.display import print_tools
from app.views.menus import TOOL_MENU


class ToolController:
    def __init__(self, tool_service, trace_service) -> None:
        self.tool_service = tool_service
        self.trace_service = trace_service

    def run(self) -> None:
        while True:
            option = ValidationService.validar_menu(TOOL_MENU, 1, 6)
            match option:
                case 1:
                    self.tool_service.create()
                    self.trace_service.log("herramienta", "crear", "Se ha registrado una herramienta nueva")
                case 2:
                    self._list_all()
                    self.tool_service.update()
                    self.trace_service.log("herramienta", "actualizar", "Se ha actualizado una herramienta")
                case 3:
                    self._list_all()
                case 4:
                    tool = self._search()
                    if tool:
                        print_tools([tool])
                case 5:
                    self._list_all()
                    self.tool_service.delete()
                    self.trace_service.log("herramienta", "eliminar", "Se ha eliminado una herramienta")
                case 6:
                    break

    def _list_all(self) -> None:
        print_tools(self.tool_service.list_all())

    def _search(self):
        tool_id = ValidationService.validar_entero("Ingrese el id a buscar: ")
        tool = self.tool_service.find_by_id(tool_id)
        if not tool:
            print("NO SE ENCONTRÓ EL ID: ", tool_id)
        return tool
