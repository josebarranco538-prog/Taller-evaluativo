#!/usr/bin/env python
# -*- coding: utf-8 -*-

from estudiantes import Estudiante
from profesores import Profesor
from MG_user import ManejadorUsuarios

print("Iniciando pruebas...")

# Crear manejador
mg = ManejadorUsuarios('usuarios.json')

# Agregar estudiantes
est1 = Estudiante('EST001', 'Juan Pérez', 'juan@email.com', '3001234567', 'MAT001', 'Ingeniería Informática', '3')
est2 = Estudiante('EST002', 'María García', 'maria@email.com', '3009876543', 'MAT002', 'Ingeniería de Sistemas', '2')

# Agregar profesores
prof1 = Profesor('PROF001', 'Dr. Carlos López', 'carlos@email.com', '3011111111', 'EMP001', 'Ingeniería', 'Programación')
prof2 = Profesor('PROF002', 'Dra. Laura Martínez', 'laura@email.com', '3022222222', 'EMP002', 'Matemáticas', 'Cálculo')

# Agregar usuarios
mg.agregar_usuario(est1)
mg.agregar_usuario(est2)
mg.agregar_usuario(prof1)
mg.agregar_usuario(prof2)

# Mostrar resumen
print(mg.mostrar_resumen())

# Pruebas de búsqueda
print('\n--- BÚSQUEDA POR ID ---')
usuario = mg.buscar_por_id('EST001')
if usuario:
    print(usuario.mostrar_perfil())

print('\n--- BÚSQUEDA POR NOMBRE ---')
resultados = mg.buscar_por_nombre('García')
print(f'Encontrados: {len(resultados)}')
for u in resultados:
    print(u.mostrar_perfil())

print('\n--- BÚSQUEDA POR TIPO ESTUDIANTE ---')
estudiantes = mg.buscar_por_tipo('estudiante')
print(f'Total estudiantes: {len(estudiantes)}')

print('\n--- BÚSQUEDA POR TIPO PROFESOR ---')
profesores = mg.buscar_por_tipo('profesor')
print(f'Total profesores: {len(profesores)}')

print('\nPruebas completadas!')
