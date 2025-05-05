function addToCart(productId) {
    fetch(`/add_to_cart/${productId}`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        updateCart(data.cartItems);
    })
    .catch(error => {
        console.error('Ошибка при добавлении товара в корзину:', error);
    });
}

function updateCart(cartItems) {
    const cartCount = document.querySelector('.cart-count');
    cartCount.textContent = `Корзина (${cartItems.length})`;
}
