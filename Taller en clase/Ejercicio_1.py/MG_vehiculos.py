


from vehiculos import Vehiculos
from bus import Bus
from taxis import Taxis
from camion import Camion
import json
from pathlib import Path


archivo = Path.home() / "Downloads" / "vehiculos.json"


def guardar_vehiculo(vehiculo, tipo):
    
    vehiculos_data = []
    with open(archivo, "r") as archivo:
        vehiculos_data = json.load(archivo)
    
    if tipo == "bus":
        atributo = vehiculo.mostrar_capacidad()
    elif tipo == "taxi":
        atributo = vehiculo.mostrar_puerta()
    elif tipo == "camion":
        atributo = vehiculo.mostrar_carga()
    
    registro = {
        "tipo": tipo,
        "placa": vehiculo.mostrar_placa(),
        "marca": vehiculo.mostrar_marca(),
        "atributo": atributo
    }
    vehiculos_data.append(registro)
    
    with open(archivo, "w") as archivo:
        json.dump(vehiculos_data, archivo, indent = 2)
    print(f" {tipo.capitalize()} guardado correctamente")


def cargar_vehiculos():
    
    vehiculos = []
    with open(archivo, "r") as archivo:
        vehiculos_data = json.load(archivo)
        for registro in vehiculos_data:
            tipo = registro["tipo"]
            placa = registro["placa"]
            marca = registro["marca"]
            atributo = registro["atributo"]
            
            if tipo == "bus":
                vehiculos.append(("bus", Bus(placa, marca, int(atributo))))
            elif tipo == "taxi":
                vehiculos.append(("taxi", Taxis(placa, marca, int(atributo))))
            elif tipo == "camion":
                vehiculos.append(("camion", Camion(placa, marca, atributo)))
    return vehiculos


def listar_vehiculos():
    
    vehiculos = cargar_vehiculos()
    if not vehiculos:
        print("No hay vehiculos guardados.")
        return
    
    print("\n---- Lista de Vehiculos ----")
    for i, (tipo, vehiculo) in enumerate(vehiculos, 1):
        print(f"\n{i}. {tipo.upper()}")
        vehiculo.mostrar_info()


def eliminar_vehiculo(indice):
    
    with open(archivo, "r") as archivo:
        vehiculos_data = json.load(archivo)
    
    if 0 <= indice < len(vehiculos_data):
        vehiculos_data.pop(indice)
        with open(archivo, "w") as archivo:
            json.dump(vehiculos_data, archivo, indent = 2)
        print("* Vehiculo eliminado")
    else:
        print("Indice invalido")






