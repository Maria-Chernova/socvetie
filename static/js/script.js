/**
 * Bloom Flowers — скрипты сайта.
 * Учебный проект для портфолио.
 */

// Плавное изменение навбара при скролле
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
    } else {
        navbar.style.boxShadow = '0 1px 10px rgba(0,0,0,0.05)';
    }
});

// Закрытие мобильного меню при клике на ссылку
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        const navCollapse = document.querySelector('.navbar-collapse');
        if (navCollapse.classList.contains('show')) {
            navCollapse.classList.remove('show');
        }
    });
});

console.log('🌸 Bloom Flowers — сайт работает!');