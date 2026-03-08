document.addEventListener('DOMContentLoaded', () => {
    // Dynamically set current year in footer and any other class instances
    const currentYearEls = document.querySelectorAll('.dynamic-year, #current-year');
    currentYearEls.forEach(el => {
        el.textContent = new Date().getFullYear();
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Dark/Light Mode Toggle
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = themeToggle.querySelector('.sun-icon');
    const moonIcon = themeToggle.querySelector('.moon-icon');
    
    // Check local storage or system preference
    const currentTheme = localStorage.getItem('theme') || "dark";
    
    if (currentTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        if (sunIcon && moonIcon) {
            sunIcon.style.display = 'block';
            moonIcon.style.display = 'none';
        }
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (sunIcon && moonIcon) {
            sunIcon.style.display = 'none';
            moonIcon.style.display = 'block';
        }
    }
    
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            let theme = document.documentElement.getAttribute('data-theme');
            if (theme === 'dark' || !theme) {
                document.documentElement.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
                if (sunIcon && moonIcon) {
                    sunIcon.style.display = 'block';
                    moonIcon.style.display = 'none';
                }
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                if (sunIcon && moonIcon) {
                    sunIcon.style.display = 'none';
                    moonIcon.style.display = 'block';
                }
            }
        });
    }

    // Interactive 3D tilt effect on service cards (Desktop Only)
    const cards = document.querySelectorAll('.service-card.interactive');
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            if (window.innerWidth < 768) return; // Disable on mobile for better performance
            
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; 
            const y = e.clientY - rect.top;  
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * -10; 
            const rotateY = ((x - centerX) / centerX) * 10;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        });
        
        card.addEventListener('mouseleave', () => {
            if (window.innerWidth < 768) return;
            card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
            card.style.transition = 'transform 0.5s ease';
            setTimeout(() => {
                card.style.transition = '';
            }, 500);
        });
    });

    // Carousel Logic
    const track = document.getElementById('carousel-track');
    const prevBtn = document.getElementById('prev-tour');
    const nextBtn = document.getElementById('next-tour');

    if (track && prevBtn && nextBtn) {
        const scrollAmount = () => {
            // Scroll by one card width
            const card = track.querySelector('.carousel-card');
            return card ? card.offsetWidth + 24 /* gap + padding avg */ : 300;
        };

        nextBtn.addEventListener('click', () => {
            track.scrollBy({ left: scrollAmount(), behavior: 'smooth' });
        });

        prevBtn.addEventListener('click', () => {
            track.scrollBy({ left: -scrollAmount(), behavior: 'smooth' });
        });
    }
});
