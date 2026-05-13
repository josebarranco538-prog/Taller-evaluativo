
import json
from MG_user import (cargar_usuarios, agregar_usuario, listar_usuarios, buscar_usuario, eliminar_usuario, actualizar_usuario)


def menu_principal():
    usuarios = cargar_usuarios()
    while True:
        
        print("---- Gestion de Usuarios ----")
        print("1. Agregar usuario generico")
        print("2. Agregar estudiante")
        print("3. Agregar profesor")
        print("4. Listar todos los usuarios")
        print("5. Buscar usuario por ID")
        print("6. Eliminar usuario")
        print("7. Actualizar usuario")
        print("8. Salir")
        opcion = int(input("Selecciona una opcion (1-8): "))
        
        match opcion:
            case 1:
                print("\n---- Agregar Usuario Generico ----")
                id_usuario = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                email = input("Email: ").strip()
                telefono = input("Telefono: ").strip()
                usuario = {
                    "id": id_usuario,
                    "nombre": nombre,
                    "email": email,
                    "telefono": telefono
                }
                agregar_usuario(usuarios, usuario)
                
            case 2:
                print("\n---- Agregar Estudiante ----")
                id_usuario = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                email = input("Email: ").strip()
                telefono = input("Telefono: ").strip()
                matricula = input("Matricula: ").strip()
                carrera = input("Carrera: ").strip()
                semestre = input("Semestre: ").strip()
                estudiante = {
                    "id": id_usuario,
                    "nombre": nombre,
                    "email": email,
                    "telefono": telefono,
                    "matricula": matricula,
                    "carrera": carrera,
                    "semestre": semestre,
                    "tipo": "estudiante"
                }
                agregar_usuario(usuarios, estudiante)
                
            case 3:
                print("\n---- Agregar Profesor ----")
                id_usuario = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                email = input("Email: ").strip()
                telefono = input("Telefono: ").strip()
                departamento = input("Departamento: ").strip()
                especialidad = input("Especialidad: ").strip()
                profesor = {
                    "id": id_usuario,
                    "nombre": nombre,
                    "email": email,
                    "telefono": telefono,
                    "departamento": departamento,
                    "especialidad": especialidad,
                    "tipo": "profesor"
                }
                agregar_usuario(usuarios, profesor)
                
            case 4:
                listar_usuarios(usuarios)
                
            case 5:
                print("\n---- Buscar Usuario ----")
                id_usuario = input("Ingresa el Id a buscar: ").strip()
                usuario = buscar_usuario(usuarios, id_usuario)
                if usuario:
                    print("\n✓ Usuario encontrado:")
                    print(json.dumps(usuario, ensure_ascii = False, indent = 2))
                else:
                    print(f" No se encontro usuario con Id: {id_usuario}")
                
            case 6:
                print("\n---- Eliminar Usuario ----")
                id_usuario = input("Ingresa el Id del usuario a eliminar: ").strip()
                eliminar_usuario(usuarios, id_usuario)
                
            case 7:
                print("\n---- Actualizar Usuario ----")
                id_usuario = input("Ingresa el Id del usuario a actualizar: ").strip()
                usuario = buscar_usuario(usuarios, id_usuario)
                if not usuario:
                    print(f" No se encontro usuario con Id: {id_usuario}")
                    break
                print("Campos disponibles para actualizar:")
                print("- nombre, email, telefono")
                if "matricula" in usuario:
                    print("- matricula, carrera, semestre")
                elif "departamento" in usuario:
                    print("- departamento, especialidad")
                campo = input("Campo a actualizar: ").strip()
                valor = input(f"Nuevo valor para {campo}: ").strip()
                actualizar_usuario(usuarios, id_usuario, {campo: valor})
                
            case 8:
                print(" Gracias, buen dia")
                break
            
            case _:
                print(" Opcion no valida")


menu_principal()





