


from vehiculos import Vehiculos

class Camion(Vehiculos):
    
    def __init__(self, placa, marca, carga):
        super().__init__(placa, marca)
        self.__carga = carga
    
    def mostrar_carga(self):
        return self.__carga
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"- Carga: {self.__carga}")






