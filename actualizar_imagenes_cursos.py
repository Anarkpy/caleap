import os

# Directorio de los cursos
dir_cursos = 'cursos'

# Obtener lista de archivos HTML en el directorio de cursos
archivos_html = [f for f in os.listdir(dir_cursos) if f.endswith('.html')]

# Para cada archivo HTML
for archivo in archivos_html:
    # Obtener el número del curso (por ejemplo, "6-1" de "6-1.html")
    nombre_curso = archivo[:-5]  # Eliminar la extensión .html
    
    # Leer el contenido del archivo
    with open(os.path.join(dir_cursos, archivo), 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Determinar la imagen correcta
    if nombre_curso in ['10-1', '10-4']:
        imagen = '../images/10-1_10-4.jpg'
    else:
        imagen = f'../images/{nombre_curso}.jpg'
    
    # Reemplazar la imagen del mapa con la imagen del curso
    contenido = contenido.replace('../images/mapa-casd.jpg', imagen)
    
    # Guardar los cambios
    with open(os.path.join(dir_cursos, archivo), 'w', encoding='utf-8') as f:
        f.write(contenido)

print("Archivos actualizados exitosamente!")
