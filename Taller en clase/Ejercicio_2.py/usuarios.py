


class Usuario:
    
    def __init__(self, id, nombre, email, telefono):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
    
    def mostrar_id(self):
        return self.__id
    
    def mostrar_nombre(self):
        return self.__nombre
    
    def mostrar_email(self):
        return self.__email
    
    def mostrar_telefono(self):
        return self.__telefono
    
    def mostrar_info(self):
        return print(f"- Id: {self.__id}\n- Nombre: {self.__nombre}\n- Email: {self.__email}\n- Teléfono: {self.__telefono}")





