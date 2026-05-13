


import json
from pathlib import Path


ruta_archivo = Path.home() / "Downloads" / "user.json"


def crear_archivo_si_no_existe():
    
    if not ruta_archivo.exists():
        print(f"Creando archivo: {ruta_archivo}")
        with open(ruta_archivo, "w", encoding = "utf-8") as u:
            json.dump([], u, ensure_ascii = False, indent = 4)
    else:
        print(f"Archivo encontrado: {ruta_archivo}")


def cargar_usuarios():
    
    crear_archivo_si_no_existe()
    with open(ruta_archivo, "r", encoding = "utf-8") as u:
        usuarios = json.load(u)
    print(f" {len(usuarios)} usuario(s) cargado(s)")
    return usuarios


def guardar_usuarios(usuarios):
    
    with open(ruta_archivo, "w", encoding = "utf-8") as u:
        json.dump(usuarios, u, ensure_ascii = False, indent = 4)
    print(" Usuarios guardados correctamente")


def agregar_usuario(usuarios, usuario):
    
    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    print(f" Usuario {usuario["nombre"]} agregado correctamente")


def listar_usuarios(usuarios):
    
    if not usuarios:
        print("No hay usuarios registrados")
        return
    
    print("---- Lista de usuarios ----")
    
    for i, usuario in enumerate(usuarios, 1):
        print(f"\n{i}. ID: {usuario["id"]}")
        print(f"    Nombre: {usuario["nombre"]}")
        print(f"    Email: {usuario["email"]}")
        print(f"    Telefono: {usuario["telefono"]}")
        
        if "matricula" in usuario:
            print(f"    Matricula: {usuario["matricula"]}")
            print(f"    Carrera: {usuario["carrera"]}")
            print(f"    Semestre: {usuario["semestre"]}")
            print(f"    Tipo: Estudiante")
        elif "departamento" in usuario:
            print(f"    Departamento: {usuario["departamento"]}")
            print(f"    Especialidad: {usuario["especialidad"]}")
            print(f"    Tipo: Profesor")
        else:
            print(f"    Tipo: Usuario generico")
    
    print(f"Total de usuarios: {len(usuarios)}")



def buscar_usuario(usuarios, id):
    
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return None


def eliminar_usuario(usuarios, id):
    
    usuario = buscar_usuario(usuarios, id)
    if usuario:
        usuarios.remove(usuario)
        guardar_usuarios(usuarios)
        print(f" Usuario {usuario["nombre"]} eliminado correctamente")
        return True
    else:
        print(f" Usuario con Id {id} no encontrado")
        return False


def actualizar_usuario(usuarios, id, datos_nuevos):
    
    usuario = buscar_usuario(usuarios, id)
    if usuario:
        usuario.update(datos_nuevos)
        guardar_usuarios(usuarios)
        print(f" Usuario actualizado correctamente")
        return True
    else:
        print(f" Usuario con Id {id} no encontrado")
        return False










