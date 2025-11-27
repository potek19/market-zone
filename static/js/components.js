// Market Zone - Django integracija
document.addEventListener('DOMContentLoaded', function() {
    // Cart functionality can be added here
    console.log('Market Zone loaded');
    // Skrolanje 
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
