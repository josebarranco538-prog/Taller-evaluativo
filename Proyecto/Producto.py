


class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = 1

    def nombre(self):
        return self.__nombre

    def precio(self):
        return self.__precio

    def cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar_producto(self):
        print(f"\n{self.__nombre}\n- ${self.__precio}\n- Cantidad: {self.__cantidad}")




