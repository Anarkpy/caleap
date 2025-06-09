import os

# Lista de cursos
cursos = [
    "6-1", "6-2", "6-3",
    "7-1", "7-2", "7-3",
    "8-1", "8-2", "8-3",
    "9-1", "9-2", "9-3", "9-4",
    "10-1", "10-2", "10-3", "10-4", "10-5", "10-6",
    "11-2", "11-3", "11-4", "11-5", "11-6"
]

# Leer la plantilla con el encoding correcto
with open('cursos/curso-template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Generar cada página de curso
for curso in cursos:
    contenido = template.replace("{{curso}}", curso)
    with open(f'cursos/{curso}.html', 'w', encoding='utf-8') as f:
        f.write(contenido)

print(f'Se han generado {len(cursos)} páginas de curso.')
