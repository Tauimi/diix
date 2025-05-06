function addToCart(productId) {
    fetch(`/add_to_cart/${productId}`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        if (data.cartItemsCount !== undefined) {
            updateCartCount(data.cartItemsCount);
        } else if (data.error) {
            console.error('Ошибка: ', data.error);
        }
    })
    .catch(error => {
        console.error('Ошибка при добавлении товара в корзину:', error);
    });
}

function updateCartCount(count) {
    const cartCountSpan = document.querySelector('.cart-count');
    if (cartCountSpan) {
        cartCountSpan.textContent = count; // Обновляем только число
    }
}
