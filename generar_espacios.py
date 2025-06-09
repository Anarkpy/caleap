import os

# Lista de espacios y sus nombres de archivo
espacios = [
    {"nombre": "Auditorio", "archivo": "auditorio.html"},
    {"nombre": "Baños Arriba", "archivo": "banos-arriba.html"},
    {"nombre": "Baños Abajo", "archivo": "banos-abajo.html"},
    {"nombre": "Cafetería", "archivo": "cafeteria.html"},
    {"nombre": "Conuco", "archivo": "conuco.html"},
    {"nombre": "Coordinación", "archivo": "coordinacion.html"},
    {"nombre": "Laboratorio de Alimentos", "archivo": "laboratorio-alimentos.html"},
    {"nombre": "Laboratorio de Química", "archivo": "laboratorio-quimica.html"},
    {"nombre": "Laboratorio de Física", "archivo": "laboratorio-fisica.html"},
    {"nombre": "Sala de Mantenimiento", "archivo": "mantenimiento.html"},
    {"nombre": "Papelería", "archivo": "papeleria.html"},
    {"nombre": "Rectoría", "archivo": "rectoria.html"},
    {"nombre": "Sala de Profesores", "archivo": "profesores.html"},
    {"nombre": "Sala de Sistemas", "archivo": "sistemas.html"},
    {"nombre": "Timbiriche", "archivo": "timbiriche.html"},
    {"nombre": "ViveDigital", "archivo": "vivedigital.html"}
]

# Leer la plantilla
template = open('otros-template.html', 'r', encoding='utf-8').read()

# Generar cada archivo de espacio
for espacio in espacios:
    contenido = template.replace('{{nombre}}', espacio['nombre'])
    with open(f'otros/{espacio["archivo"]}', 'w', encoding='utf-8') as f:
        f.write(contenido)

print("Archivos generados exitosamente!")
