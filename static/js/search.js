document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form[action*="search"]');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        const query = form.query.value.trim();
        if (query.length < 2) {
            alert('Введите не менее 2 символов для поиска.');
            e.preventDefault();
        }
    });
}); 