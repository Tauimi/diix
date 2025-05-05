
let currentSlide = 0;

function moveSlide(direction) {
    const slides = document.querySelectorAll('.news-item');
    const totalSlides = slides.length;

    currentSlide += direction;

    if (currentSlide < 0) {
        currentSlide = totalSlides - 1; // Перемещаем в конец
    }

    if (currentSlide >= totalSlides) {
        currentSlide = 0; // Перемещаем в начало
    }

    const newTransformValue = -currentSlide * 100;
    document.querySelector('.news-container').style.transform = `translateX(${newTransformValue}%)`;
}

// Автоматическое переключение слайдов каждые 5 секунд
setInterval(() => {
    moveSlide(1);
}, 5000);
