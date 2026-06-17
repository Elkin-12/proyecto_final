document.addEventListener("DOMContentLoaded", function() {
    const currentPath = window.location.pathname;
    const links = document.querySelectorAll(".nav-links a");
        links.forEach(link => {
          const href = link.getAttribute("href");
            if (href) {
            if (currentPath === href || 
                (currentPath.includes('/clientes/') && href.includes('clientes')) ||
                (currentPath.includes('/medicos/') && href.includes('medicos') && !currentPath.includes('/medicos/')) ||
                (currentPath.includes('/citas/') && href.includes('citas') && !currentPath.includes('/citas/')) ||
                (currentPath.includes('/servicios/') && href.includes('servicios')) ||
                (currentPath.includes('/especialidades/') && href.includes('especialidades'))) {
                   link.classList.add("active");
                    } else {
                        link.classList.remove("active");
                    }
                }
            });
        });