import os
from shutil import copy2

def generar_paginas_otros():
    # Lista de espacios y sus datos
    espacios = {
        "auditorio": {"nombre": "Auditorio", "imagen": "auditorio.jpg", "descripcion": "Espacio para eventos y presentaciones"},
        "banos-arriba": {"nombre": "Baños Arriba", "imagen": "banos-arriba.jpg", "descripcion": "Baños del segundo piso"},
        "banos-abajo": {"nombre": "Baños Abajo", "imagen": "banos-abajo.jpg", "descripcion": "Baños del primer piso"},
        "cafeteria": {"nombre": "Cafetería", "imagen": "cafeteria.jpg", "descripcion": "Espacio para comer y socializar"},
        "conuco": {"nombre": "Conuco", "imagen": "conuco.jpg", "descripcion": "Área de recreación al aire libre"},
        "coordinacion": {"nombre": "Coordinación", "imagen": "coordinacion.jpg", "descripcion": "Oficina de coordinación escolar"},
        "lab-alimentos": {"nombre": "Laboratorio de Alimentos", "imagen": "lab-alimentos.jpg", "descripcion": "Laboratorio para prácticas culinarias"},
        "lab-quimica": {"nombre": "Laboratorio de Química", "imagen": "lab-quimica.jpg", "descripcion": "Laboratorio para experimentos químicos"},
        "lab-fisica": {"nombre": "Laboratorio de Física", "imagen": "lab-fisica.jpg", "descripcion": "Laboratorio para experimentos físicos"},
        "mantenimiento": {"nombre": "Sala de Mantenimiento", "imagen": "mantenimiento.jpg", "descripcion": "Área para mantenimiento del colegio"},
        "papeleria": {"nombre": "Papelería", "imagen": "papeleria.jpg", "descripcion": "Tienda de suministros escolares"},
        "rectoria": {"nombre": "Rectoría", "imagen": "rectoria.jpg", "descripcion": "Oficina de rectoría"},
        "profesores": {"nombre": "Sala de Profesores", "imagen": "profesores.jpg", "descripcion": "Espacio para profesores"},
        "sistemas": {"nombre": "Sala de Sistemas", "imagen": "sistemas.jpg", "descripcion": "Área de soporte técnico"},
        "timbiriche": {"nombre": "Timbiriche", "imagen": "timbiriche.jpg", "descripcion": "Espacio para actividades infantiles"},
        "vivedigital": {"nombre": "ViveDigital", "imagen": "vivedigital.jpg", "descripcion": "Espacio para actividades digitales"}
    }

    # Crear la carpeta otros si no existe
    if not os.path.exists('otros'):
        os.makedirs('otros')

    # Copiar la plantilla
    copy2('otros-template.html', 'otros/template.html')

    # Generar cada página
    for nombre, datos in espacios.items():
        with open(f'otros/template.html', 'r', encoding='utf-8') as template:
            contenido = template.read()
            
            # Reemplazar los placeholders
            contenido = contenido.replace("Nombre del Espacio", datos["nombre"])
            contenido = contenido.replace("Espacio", datos["nombre"])
            contenido = contenido.replace("Descripción del espacio...", datos["descripcion"])
            
            # Guardar la página
            with open(f'otros/{nombre}.html', 'w', encoding='utf-8') as pagina:
                pagina.write(contenido)

    # Eliminar la plantilla temporal
    os.remove('otros/template.html')

    print("Páginas generadas exitosamente!")

if __name__ == "__main__":
    generar_paginas_otros()
