// Adiciona animação de rolagem para exibir elementos da linha do tempo gradualmente
window.addEventListener('scroll', function() {
    const timelineItems = document.querySelectorAll('.timeline-item');

    timelineItems.forEach(item => {
        const itemPosition = item.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;

        if (itemPosition < windowHeight - 100) {
            item.classList.add('active');
        }
    });
});
