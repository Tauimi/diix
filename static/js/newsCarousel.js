let currentIndex = 0;

const newsItems = document.querySelectorAll('.news-item');
const totalItems = newsItems.length;

const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

function updateCarousel() {
    const offset = -currentIndex * 100;
    document.querySelector('.news-container').style.transform = `translateX(${offset}%)`;
}

prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex === 0) ? totalItems - 1 : currentIndex - 1;
    updateCarousel();
});

nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex === totalItems - 1) ? 0 : currentIndex + 1;
    updateCarousel();
});

updateCarousel();
