
function addToCart(productId) {
    fetch(`/add_to_cart/${productId}`, {
        method: 'GET'
    })
    .then(response => {
        alert("Товар добавлен в корзину");
        location.reload();
    });
}
