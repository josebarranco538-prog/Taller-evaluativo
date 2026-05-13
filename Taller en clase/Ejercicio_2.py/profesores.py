


from usuarios import Usuario

class Profesor(Usuario):
    
    def __init__(self, id, nombre, email, telefono, departamento, especialidad):
        super().__init__(id, nombre, email, telefono)
        self.__departamento = departamento
        self.__especialidad = especialidad
    
    def mostrar_departamento(self):
        return self.__departamento
    
    def mostrar_especialidad(self):
        return self.__especialidad
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"- Departamento: {self.__departamento}\n- Especialidad: {self.__especialidad}")





