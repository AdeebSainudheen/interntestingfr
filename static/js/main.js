const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('open');
    });
}

const scrollLinks = document.querySelectorAll('.nav-links a');
scrollLinks.forEach(link => {
    link.addEventListener('click', event => {
        const targetId = link.getAttribute('href');
        if (targetId.startsWith('#')) {
            event.preventDefault();
            document.querySelector(targetId)?.scrollIntoView({ behavior: 'smooth' });
            navLinks.classList.remove('open');
        }
    });
});
