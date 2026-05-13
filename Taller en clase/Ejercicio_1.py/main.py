


from MG_vehiculos import guardar_vehiculo, listar_vehiculos, eliminar_vehiculo
from bus import Bus
from taxis import Taxis
from camion import Camion

def menu():
    
    while True:
        print("\n---- Menu de vehiculos----")
        print("1. Guardar Bus")
        print("2. Guardar Taxi")
        print("3. Guardar Camion")
        print("4. Listar vehiculos")
        print("5. Eliminar vehiculo")
        print("6. Salir")
        
        opcion = int(input("\nElige una opcion: "))
        
        match opcion:
            case 1:
                placa = input("Placa: ")
                marca = input("Marca: ")
                capacidad = int(input("Capacidad: "))
                bus = Bus(placa, marca, capacidad)
                guardar_vehiculo(bus, "bus")
            
            case 2:
                placa = input("Placa: ")
                marca = input("Marca: ")
                puertas = int(input("Puertas: "))
                taxi = Taxis(placa, marca, puertas)
                guardar_vehiculo(taxi, "taxi")
            
            case 3:
                placa = input("Placa: ")
                marca = input("Marca: ")
                carga = input("Carga: ")
                camion = Camion(placa, marca, carga)
                guardar_vehiculo(camion, "camion")
            
            case 4:
                listar_vehiculos()
            
            case 5:
                listar_vehiculos()
                indice = int(input("\nIndice a eliminar: ")) - 1
                eliminar_vehiculo(indice)
            
            case 6:
                print("Gracias, buen dia")
                break
            
            case _:
                print("Opcion invalida")

menu()





