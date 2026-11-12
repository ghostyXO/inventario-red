from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Dispositivo(BaseModel):
    nombre: str
    tipo: str
    ip: str
    activo: bool

inventario = [
    Dispositivo(nombre="R1", tipo="router", ip="192.168.1.1", activo=True),
    Dispositivo(nombre="SW1", tipo="switch", ip="192.168.1.2", activo=True)
]

def buscar(nombre: str):
    """Devuelve el equipo con ese nombre, o None si no existe."""
    for equipo in inventario:
        if equipo.nombre.upper() == nombre.upper():
            return equipo
    return None

@app.get("/dispositivos")
async def listar():
    return inventario

@app.get("/dispositivos/{nombre}")
async def obtener(nombre: str):
    equipo = buscar(nombre)
    if equipo is None:
        raise HTTPException(status_code=404, detail=f"No existe el equipo {nombre}")
    return equipo
