function updateTotal() {
    const select = document.getElementById('product');
    const price = parseInt(select.options[select.selectedIndex].getAttribute('data-price'));
    const quantity = parseInt(document.getElementById('quantity').value) || 1;
    document.getElementById('total').textContent = price * quantity;
}
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('product').addEventListener('change', updateTotal);
    document.getElementById('quantity').addEventListener('input', updateTotal);
    updateTotal();

    const form = document.getElementById('calc-form');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        let valid = true;
        let messages = [];

        const quantity = form.quantity.value;
        if (!quantity || isNaN(quantity) || parseInt(quantity) < 1) {
            valid = false;
            messages.push('Введите корректное количество (целое число больше 0).');
        }

        if (!valid) {
            alert(messages.join('\n'));
            e.preventDefault();
        }
    });
}); 