import os

# Mapeo de nombres de archivo a rutas de imagen
mapeo_imagenes = {
    'auditorio.html': 'auditorio.jpg',
    'banos-abajo.html': 'baños.jpg',  # Asumiendo que baños.jpg es para abajo
    'banos-arriba.html': 'baños2.jpg',  # Y baños2.jpg para arriba
    'cafeteria.html': 'cafeteria.jpg',
    'conuco.html': 'conuco.jpg',
    'coordinacion.html': 'coordinacion.jpg',
    'lab-alimentos.html': 'lab_alimentos.jpg',
    'lab-fisica.html': 'lab-fisica.jpg',
    'lab-quimica.html': 'lab_quimica.jpg',
    'mantenimiento.html': 'mantenimiento.jpg',
    'papeleria.html': 'papeleria.jpg',
    'profesores.html': 'sala_profesores.jpg',
    'rectoria.html': 'rectoria.jpg',
    'sistemas.html': 'sala_sistemas.jpg',
    'timbiriche.html': 'timbiriche.jpg',
    'vivedigital.html': 'vive_digital.jpg'
}

dir_otros = 'otros'

# Actualizar cada archivo HTML
for archivo, imagen in mapeo_imagenes.items():
    ruta_archivo = os.path.join(dir_otros, archivo)
    
    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        print(f"Advertencia: {ruta_archivo} no existe, omitiendo...")
        continue
    
    # Leer el contenido actual
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Reemplazar la imagen
    nuevo_contenido = contenido.replace(
        '../images/mapa-casd.jpg', 
        f'../images/{imagen}'
    )
    
    # Actualizar el título de la imagen
    titulo = os.path.splitext(archivo)[0].replace('-', ' ').title()
    nuevo_contenido = nuevo_contenido.replace(
        'alt="Mapa del Colegio CASD"',
        f'alt="Ubicación de {titulo}"'
    )
    
    # Guardar los cambios
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)
    
    print(f"Actualizado: {archivo} -> {imagen}")

print("\nProceso completado. Se actualizaron las imágenes en las páginas.")
print("Nota: Algunos archivos pueden no haberse actualizado si no existen en la carpeta 'otros'.")
