// Naloži navbar in footer komponente
async function loadComponent(componentName, targetId) {
    try {
        const response = await fetch(`components/${componentName}.html`);
        if (!response.ok) {
            throw new Error(`Failed to load ${componentName}`);
        }
        const html = await response.text();
        document.getElementById(targetId).innerHTML = html;
        
        // Posodobi aktivno povezavo v navbaru
        if (componentName === 'navbar') {
            updateActiveNavLink();
        }
    } catch (error) {
        console.error(`Error loading ${componentName}:`, error);
    }
}

// Označi trenutno aktivno stran v navigaciji
function updateActiveNavLink() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Ko se stran naloži, naloži navbar in footer
document.addEventListener('DOMContentLoaded', function() {
    loadComponent('navbar', 'navbar-placeholder');
    loadComponent('footer', 'footer-placeholder');
});
