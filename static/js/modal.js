
// Функция для открытия модального окна
function openModal(modalId) {
    document.getElementById(modalId).style.display = "block";
}

// Функция для закрытия модального окна
function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

// Открытие модального окна входа при нажатии на "Вход"
document.getElementById('login').addEventListener('click', function() {
    openModal('loginModal');
});

// Открытие модального окна регистрации при нажатии на "Регистрация"
document.getElementById('register').addEventListener('click', function() {
    openModal('registerModal');
});

// Закрытие модальных окон при клике за пределами окна
window.onclick = function(event) {
    if (event.target == document.getElementById('loginModal')) {
        closeModal('loginModal');
    } else if (event.target == document.getElementById('registerModal')) {
        closeModal('registerModal');
    }
}
