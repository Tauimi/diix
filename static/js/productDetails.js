
let currentProduct = null;

function showProductDetails(productId) {
    currentProduct = products.find(product => product.id === productId);
    document.getElementById('productName').textContent = currentProduct.name;
    document.getElementById('productDescription').textContent = currentProduct.description;
    document.getElementById('productPrice').textContent = `Цена: ${currentProduct.price} руб`;
    document.getElementById('productModal').style.display = "block";
}

function closeModal() {
    document.getElementById('productModal').style.display = "none";
}

window.onclick = function(event) {
    if (event.target == document.getElementById('productModal')) {
        closeModal();
    }
}
