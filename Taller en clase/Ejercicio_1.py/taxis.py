

from vehiculos import Vehiculos

class Taxis(Vehiculos):
    
    def __init__(self, placa, marca, puerta):
        super().__init__(placa, marca)
        self.__puerta = puerta
    
    def mostrar_puerta(self):
        return self.__puerta
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"- Puertas: {self.__puerta}")








