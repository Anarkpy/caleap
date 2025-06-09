const fs = require('fs');

// Lista de cursos
const cursos = [
    "6-1", "6-2", "6-3",
    "7-1", "7-2", "7-3",
    "8-1", "8-2", "8-3",
    "9-1", "9-2", "9-3", "9-4",
    "10-1", "10-2", "10-3", "10-4", "10-5", "10-6",
    "11-2", "11-3", "11-4", "11-5", "11-6"
];

// Leer la plantilla
const template = fs.readFileSync('cursos/curso-template.html', 'utf8');

// Generar cada página de curso
for (const curso of cursos) {
    const contenido = template.replace("{{curso}}", curso);
    fs.writeFileSync(`cursos/${curso}.html`, contenido);
}

console.log(`Se han generado ${cursos.length} páginas de curso.`);
