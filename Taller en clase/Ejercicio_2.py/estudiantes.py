


from usuarios import Usuario

class Estudiante(Usuario):
    
    def __init__(self, id, nombre, email, telefono, matricula, carrera, semestre):
        super().__init__(id, nombre, email, telefono)
        self.__matricula = matricula
        self.__carrera = carrera
        self.__semestre = semestre
    
    def mostrar_matricula(self):
        return self.__matricula
    
    def mostrar_carrera(self):
        return self.__carrera
    
    def mostrar_semestre(self):
        return self.__semestre
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"- Matrícula: {self.__matricula}\n- Carrera: {self.__carrera}\n- Semestre: {self.__semestre}")





