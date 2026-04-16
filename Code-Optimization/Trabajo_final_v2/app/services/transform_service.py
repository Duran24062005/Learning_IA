from app.services.validation_service import ValidationService


class TransformService:
    @staticmethod
    def transformar_estado(estado: int) -> str:
        if estado == 1:
            return "Activo"
        if estado == 2:
            return "En reparación"
        return "Inactiva"

    @staticmethod
    def transformar_tipo(tipo: int) -> str:
        if tipo == 1:
            return "Residente"
        return "Administrador"

    @staticmethod
    def solicitar_fecha_inicio():
        return ValidationService.solicitar_fecha_inicio()
