// Функция для фильтрации товаров по категории
function filterProducts() {
    const category = document.getElementById('category').value;
    const price = document.getElementById('price').value;
    
    const products = document.querySelectorAll('.product-item');
    
    // Фильтрация товаров по категории
    products.forEach(product => {
        const productCategory = product.getAttribute('data-category');
        const productPrice = parseInt(product.getAttribute('data-price'));
        
        if (category === 'all' || category === productCategory) {
            product.style.display = 'block';  // Показываем товар
        } else {
            product.style.display = 'none';  // Скрываем товар
        }
    });

    // Сортировка товаров по цене
    const sortedProducts = Array.from(products).sort((a, b) => {
        const priceA = parseInt(a.getAttribute('data-price'));
        const priceB = parseInt(b.getAttribute('data-price'));
        
        if (price === 'asc') {
            return priceA - priceB;
        } else if (price === 'desc') {
            return priceB - priceA;
        }
    });

    // Перезаписываем порядок отображения товаров
    const productList = document.getElementById('product-list');
    sortedProducts.forEach(product => {
        productList.appendChild(product);
    });
}

// Инициализация событий для фильтров
document.getElementById('category').addEventListener('change', filterProducts);
document.getElementById('price').addEventListener('change', filterProducts);

// Инициализируем фильтрацию при загрузке страницы
filterProducts();
