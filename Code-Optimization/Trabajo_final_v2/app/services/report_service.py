class ReportService:
    def __init__(self, tool_repository, loan_repository, user_repository) -> None:
        self.tool_repository = tool_repository
        self.loan_repository = loan_repository
        self.user_repository = user_repository

    def stock_minimo(self, stock: int) -> list[dict]:
        records = self.tool_repository.load_all()
        if not records:
            print("No se puede buscar porque no hay registros")
            return []
        results = []
        for record in records:
            if record.get("cantidad", "clave no encontrada") <= stock:
                results.append(record)
                return results
        print("NO SE ENCONTRÓ NINGÚN STOCK CON ESA CANTIDAD MINIMA: ", stock)
        return results

    def prestamos_por_estado(self, option: int) -> list[dict]:
        records = self.loan_repository.load_all()
        if not records:
            print("No se puede buscar porque no hay registros")
            return []
        results = []
        match option:
            case 1:
                for record in records:
                    if record.get("estado", "clave no encontrada") == "En proceso":
                        results.append(record)
                    else:
                        print("NO SE ENCONTRO NINGUN PRESTAMO EN ESTADO DE: EN PROCESO")
            case 2:
                for record in records:
                    if record.get("estado", "clave no encontrada") in {"Aceptada", "Rechazada"}:
                        results.append(record)
                    else:
                        print("NO SE ENCONTRÓ NINGUN PRESTAAMO EN ESTADO: COMPLETADA O RECHAZADA")
        return results

    def historial_usuario(self, user_id: int) -> list[dict]:
        records = self.loan_repository.load_all()
        if not records:
            print("No hay registros en este momento")
            return []
        results = []
        for record in records:
            if record.get("usuario", "Clave no encontrada").get("id", "id de usuario no encontrado") == user_id:
                results.append(record)
        return results

    def herramienta_mas_usada(self) -> list[str]:
        tools = self.tool_repository.load_all()
        records = self.loan_repository.load_all()
        if not records:
            print("No hay registros en este momento")
            return []
        results = []
        for tool in tools:
            contador = 0
            for loan in records:
                if tool["id"] == loan["herramienta"]["id"]:
                    contador += 1
            if contador > 0:
                results.append(f"{tool['id']}, {tool['nombre']} = {contador}\n")
        return results

    def usuario_mas_usado(self) -> list[str]:
        users = self.user_repository.load_all()
        records = self.loan_repository.load_all()
        if not records:
            print("No hay registros en este momento")
            return []
        results = []
        for user in users:
            contador = 0
            for loan in records:
                if user["id"] == loan["usuario"]["id"]:
                    contador += 1
            if contador > 0:
                results.append(f"{user['id']}, {user['nombre']} {user['apellido']} = {contador}\n")
        return results
