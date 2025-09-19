// Verificar que el archivo se está cargando
console.log('main.js cargado');

// Datos de ejemplo para cursos (reemplázalos con los tuyos)
const cursos = [
    { nombre: "6-1", ruta: "cursos/6-1.html" },
    { nombre: "6-2", ruta: "cursos/6-2.html" },
    { nombre: "6-3", ruta: "cursos/6-3.html" },
    { nombre: "7-1", ruta: "cursos/7-1.html" },
    { nombre: "7-2", ruta: "cursos/7-2.html" },
    { nombre: "7-3", ruta: "cursos/7-3.html" },
    { nombre: "8-1", ruta: "cursos/8-1.html" },
    { nombre: "8-2", ruta: "cursos/8-2.html" },
    { nombre: "8-3", ruta: "cursos/8-3.html" },
    { nombre: "9-1", ruta: "cursos/9-1.html" },
    { nombre: "9-2", ruta: "cursos/9-2.html" },
    { nombre: "9-3", ruta: "cursos/9-3.html" },
    { nombre: "9-4", ruta: "cursos/9-4.html" },
    { nombre: "10-1", ruta: "cursos/10-1.html" },
    { nombre: "10-2", ruta: "cursos/10-2.html" },
    { nombre: "10-3", ruta: "cursos/10-3.html" },
    { nombre: "10-4", ruta: "cursos/10-4.html" },
    { nombre: "10-5", ruta: "cursos/10-5.html" },
    { nombre: "10-6", ruta: "cursos/10-6.html" },
    { nombre: "11-2", ruta: "cursos/11-2.html" },
    { nombre: "11-3", ruta: "cursos/11-3.html" },
    { nombre: "11-4", ruta: "cursos/11-4.html" },
    { nombre: "11-5", ruta: "cursos/11-5.html" },
    { nombre: "11-6", ruta: "cursos/11-6.html" }
];

// Datos de ejemplo para otros espacios (reemplázalos con los tuyos)
const otrosEspacios = [
    { nombre: "Auditorio", ruta: "otros/auditorio.html" },
    { nombre: "Baños Arriba", ruta: "otros/banos-arriba.html" },
    { nombre: "Baños Abajo", ruta: "otros/banos-abajo.html" },
    { nombre: "Cafetería", ruta: "otros/cafeteria.html" },
    { nombre: "Conuco", ruta: "otros/conuco.html" },
    { nombre: "Coordinación", ruta: "otros/coordinacion.html" },
    { nombre: "Laboratorio de Alimentos", ruta: "otros/laboratorio-alimentos.html" },
    { nombre: "Laboratorio de Química", ruta: "otros/laboratorio-quimica.html" },
    { nombre: "Laboratorio de Física", ruta: "otros/laboratorio-fisica.html" },
    { nombre: "Sala de Mantenimiento", ruta: "otros/mantenimiento.html" },
    { nombre: "Papelería", ruta: "otros/papeleria.html" },
    { nombre: "Rectoría", ruta: "otros/rectoria.html" },
    { nombre: "Sala de Profesores", ruta: "otros/profesores.html" },
    { nombre: "Sala de Sistemas", ruta: "otros/sistemas.html" },
    { nombre: "Timbiriche", ruta: "otros/timbiriche.html" },
    { nombre: "ViveDigital", ruta: "otros/vivedigital.html" }
];

// Función para agrupar cursos por grado
function agruparCursosPorGrado() {
    const grupos = {};
    cursos.forEach(curso => {
        const grado = curso.nombre.split('-')[0];
        if (!grupos[grado]) {
            grupos[grado] = [];
        }
        grupos[grado].push(curso);
    });
    return grupos;
}

// Función para mostrar los cursos
function mostrarCursos() {
    const listaCursos = document.getElementById('listaCursos');
    if (!listaCursos) return; // Si no existe, salir

    const grupos = agruparCursosPorGrado();
    const gradosOrdenados = Object.keys(grupos).sort((a, b) => parseInt(a) - parseInt(b));

    // Si no hay cursos, mostrar mensaje
    if (gradosOrdenados.length === 0) {
        listaCursos.innerHTML = '<div class="alert alert-info">No hay cursos disponibles.</div>';
        return;
    }

    gradosOrdenados.forEach(grado => {
        const button = document.createElement('button');
        button.className = 'btn btn-outline-primary w-100 mb-2 text-start';
        button.type = 'button';
        button.setAttribute('data-bs-toggle', 'collapse');
        button.setAttribute('data-bs-target', `#cursos-${grado}`);
        button.setAttribute('aria-expanded', 'false');
        button.setAttribute('aria-controls', `cursos-${grado}`);
        button.innerHTML = `
            <div class="d-flex justify-content-between align-items-center">
                <span>Grado ${grado}</span>
                <i class="fas fa-chevron-down"></i>
            </div>
        `;

        const divCursos = document.createElement('div');
        divCursos.className = 'collapse mb-3';
        divCursos.id = `cursos-${grado}`;

        const ul = document.createElement('ul');
        ul.className = 'list-group';

        // Ordenar cursos por sección (A, B, etc.)
        const cursosOrdenados = [...grupos[grado]].sort((a, b) => 
            a.nombre.localeCompare(b.nombre)
        );

        cursosOrdenados.forEach(curso => {
            const li = document.createElement('li');
            li.className = 'list-group-item position-relative';

            // Crear el enlace que cubre todo el item
            const a = document.createElement('a');
            a.href = curso.ruta;
            a.className = 'text-decoration-none stretched-link';
            a.textContent = curso.nombre;

            li.appendChild(a);
            ul.appendChild(li);
        });

        divCursos.appendChild(ul);
        listaCursos.appendChild(button);
        listaCursos.appendChild(divCursos);

        // Sincronizar icono y aria-expanded con eventos de Bootstrap Collapse
        const collapseInstance = new bootstrap.Collapse(divCursos, { toggle: false });
        divCursos.addEventListener('show.bs.collapse', () => {
            button.setAttribute('aria-expanded', 'true');
            const icon = button.querySelector('i');
            if (icon) icon.classList.add('fa-rotate-180');
        });
        divCursos.addEventListener('hide.bs.collapse', () => {
            button.setAttribute('aria-expanded', 'false');
            const icon = button.querySelector('i');
            if (icon) icon.classList.remove('fa-rotate-180');
        });
    });
}

// Función para mostrar otros espacios
function mostrarOtros() {
    const listaOtros = document.getElementById('listaOtros');
    if (!listaOtros) return; // Si no existe, salir

    // Si no hay espacios, mostrar mensaje
    if (otrosEspacios.length === 0) {
        listaOtros.innerHTML = '<div class="alert alert-info">No hay espacios disponibles.</div>';
        return;
    }

    const ul = document.createElement('ul');
    ul.className = 'list-group';

    // Ordenar espacios alfabéticamente
    const espaciosOrdenados = [...otrosEspacios].sort((a, b) => 
        a.nombre.localeCompare(b.nombre)
    );

    espaciosOrdenados.forEach(espacio => {
        const li = document.createElement('li');
        li.className = 'list-group-item position-relative';
        const a = document.createElement('a');
        a.href = espacio.ruta;
        a.className = 'text-decoration-none d-block stretched-link';
        a.textContent = espacio.nombre;
        li.appendChild(a);
        ul.appendChild(li);
    });

    listaOtros.appendChild(ul);
}

// Inicialización
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips de Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Mostrar contenido dinámico
    mostrarCursos();
    mostrarOtros();
});

// Fin del archivo
