from datetime import date


class ValidationService:
    @staticmethod
    def validar_entero(mensaje: str) -> int:
        while True:
            try:
                dato = int(input(mensaje))
                while dato <= 0:
                    dato = int(input("Error. Ingrese un numero positivo: "))
                return dato
            except Exception:
                print("Error, solo se admiten número entero.")

    @staticmethod
    def validar_decimales(mensaje: str) -> float:
        while True:
            try:
                dato = float(input(mensaje))
                while dato <= 0:
                    dato = float(input("Error. Ingrese un numero positivo real: "))
                return dato
            except Exception:
                print("Error, solo se admiten números decimales.")

    @staticmethod
    def validar_texto(mensaje: str, cantidad_minima: int, cantidad_maxima: int) -> str:
        try:
            dato = input(mensaje)
            caracteres = len(dato.strip())
            while caracteres < cantidad_minima or caracteres > cantidad_maxima or dato is None:
                dato = input("Error, no puede dejar el espacio en blanco: ")
                caracteres = len(dato.strip())
            return dato
        except Exception:
            print("Error, solo se admite texto")
            return ""

    @classmethod
    def validar_menu(cls, mensaje: str, minimo: int, maximo: int) -> int:
        op = cls.validar_entero(mensaje)
        while op < minimo or op > maximo:
            op = cls.validar_entero("Error intentelo nuevamente: ")
        return op

    @classmethod
    def solicitar_fecha_inicio(cls) -> date:
        anio = cls.validar_entero("Ingrese el año de la solicitud: ")
        mes = cls.validar_entero("Ingrese el mes de la solicitud: ")
        dia = cls.validar_entero("Ingrese el dia de la solicitud: ")
        return date(anio, mes, dia)
