const navSlide = () => {
    const menu = document.querySelector('.menu');
    const nav = document.querySelector('.navLinks');
    const links = document.querySelectorAll('.navLinks li');

    menu.addEventListener('click', () => {
        nav.classList.toggle('active');
        links.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            }
            else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`
            }
        });

        menu.classList.toggle('toggle');
    })
}

navSlide();