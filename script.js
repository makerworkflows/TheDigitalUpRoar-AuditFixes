document.addEventListener('DOMContentLoaded', () => {
    // Dynamic year
    const yearEl = document.getElementById('current-year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
    });

    // Carousel
    const track = document.getElementById('carousel-track');
    const prevBtn = document.getElementById('prev-tour');
    const nextBtn = document.getElementById('next-tour');

    if (track && prevBtn && nextBtn) {
        const scrollAmount = () => {
            const card = track.querySelector('.carousel-card');
            return card ? card.offsetWidth + 24 : 300;
        };

        nextBtn.addEventListener('click', () => {
            track.scrollBy({ left: scrollAmount(), behavior: 'smooth' });
        });

        prevBtn.addEventListener('click', () => {
            track.scrollBy({ left: -scrollAmount(), behavior: 'smooth' });
        });
    }
});
