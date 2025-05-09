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
        cartCountSpan.textContent = count;
    }
}

// Удаление одного товара
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('remove-item')) {
        const productId = e.target.getAttribute('data-product-id');
        fetch(`/remove_from_cart/${productId}`, { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Удаляем товар из DOM
                    const item = e.target.closest('.cart-item');
                    if (item) item.remove();
                    updateCartCount(data.cartItemsCount);

                    // Если корзина пуста — скрываем блок с товарами, показываем "пуста"
                    if (data.cartItemsCount === 0) {
                        document.getElementById('cart-items-container').style.display = 'none';
                        document.getElementById('cart-empty').style.display = 'block';
                    }
                }
            });
    }
});

// Очистка всей корзины
document.addEventListener('DOMContentLoaded', function() {
    const clearBtn = document.getElementById('clear-cart');
    if (clearBtn) {
        clearBtn.addEventListener('click', function() {
            if (confirm('Вы уверены, что хотите очистить всю корзину?')) {
                fetch('/clear_cart', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            updateCartCount(0);
                            document.getElementById('cart-items-container').style.display = 'none';
                            document.getElementById('cart-empty').style.display = 'block';
                        }
                    });
            }
        });
    }
});
