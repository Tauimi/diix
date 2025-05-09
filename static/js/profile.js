document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.profile-form');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        let valid = true;
        let messages = [];

        const email = form.email.value.trim();
        const emailPattern = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
        if (!emailPattern.test(email)) {
            valid = false;
            messages.push('Введите корректный email.');
        }

        if (!valid) {
            alert(messages.join('\n'));
            e.preventDefault();
        }
    });
}); 