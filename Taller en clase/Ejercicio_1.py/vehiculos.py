


class Vehiculos:
    
    def __init__(self, placa, marca):
        self.__placa = placa
        self.__marca = marca
    
    def mostrar_placa(self):
        return self.__placa
    
    def mostrar_marca(self):
        return self.__marca
    
    def mostrar_info(self):
        return print(f"- Placa: {self.__placa}\n- Marca: {self.__marca}")






