from dataclasses import dataclass


@dataclass
class CategoryRecord:
    id: int
    nombre: str

    def to_dict(self) -> dict:
        return {"id": self.id, "nombre": self.nombre}


@dataclass
class UserRecord:
    id: int
    nombre: str
    apellido: str
    telefono: int
    direccion: str
    tipo: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "tipo": self.tipo,
        }


@dataclass
class ToolRecord:
    id: int
    nombre: str
    categoria: dict
    cantidad: int
    estado: str
    precio: int

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "cantidad": self.cantidad,
            "estado": self.estado,
            "precio": self.precio,
        }


@dataclass
class LoanRecord:
    id: int
    usuario: dict
    herramienta: dict
    cantidad: int
    fecha_inicio: str
    fecha_final: str
    estado: str
    observaciones: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "usuario": self.usuario,
            "herramienta": self.herramienta,
            "cantidad": self.cantidad,
            "fecha_inicio": self.fecha_inicio,
            "fecha_final": self.fecha_final,
            "estado": self.estado,
            "observaciones": self.observaciones,
        }


@dataclass
class SessionRecord:
    role: str
