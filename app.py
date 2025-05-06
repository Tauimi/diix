from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import hashlib
import datetime # Import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Для использования сессий

# Временная база данных пользователей
users_db = {}

# Счетчик посещений
visitor_count = 0

# Временная база данных товаров (для примера)
# В реальном приложении это будет база данных
products_db = {
    1: {'id': 1, 'name': 'Смартфон Galaxy S21', 'description': 'Отличная камера и экран.', 'price': 69990, 'category': 'smartphones', 'image': 'images/smartphone.jpg'},
    2: {'id': 2, 'name': 'Ноутбук Dell XPS 13', 'description': 'Легкий и мощный.', 'price': 89990, 'category': 'laptops', 'image': 'images/laptop.jpg'},
    3: {'id': 3, 'name': 'Телевизор Samsung QLED 55"', 'description': 'Невероятная цветопередача.', 'price': 49990, 'category': 'tv', 'image': 'images/tv.jpg'}
}

# Helper function to get username and visitor count
def get_context():
    # Initialize cart if not present
    if 'cart' not in session:
        session['cart'] = []
        
    current_year = datetime.datetime.now().year # Get current year

    return {
        'username': session.get('username'),
        'visitor_count': visitor_count,
        'cart_items_count': len(session.get('cart', [])), # Count items in cart
        'current_year': current_year # Add current year to context
    }

# Главная страница
@app.route('/')
def home():
    global visitor_count
    if 'visited' not in session:
        visitor_count += 1
        session['visited'] = True
    context = get_context()
    return render_template('index.html', **context)

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
             error = 'Требуется имя пользователя и пароль.'
        elif username in users_db:
            error = 'Пользователь уже существует.'
        else:
            # Сохраняем пользователя с хешированием пароля
            users_db[username] = hashlib.sha256(password.encode()).hexdigest()
            session['username'] = username  # Сохраняем пользователя в сессии
            # Redirect to profile page after successful registration
            return redirect(url_for('profile'))
            
    # For GET request or if POST fails, render the registration page
    context = get_context()
    return render_template('register.html', error=error, **context)

# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
             error = 'Требуется имя пользователя и пароль.'
        # Проверка, если пользователь существует
        elif username not in users_db:
            error = 'Пользователь не найден.'
        # Проверка пароля
        elif users_db[username] == hashlib.sha256(password.encode()).hexdigest():
            session['username'] = username  # Сохраняем пользователя в сессии
            # Redirect to profile page after successful login
            return redirect(url_for('profile')) 
        else:
            error = 'Неверный пароль.'
            
    # For GET request or if POST fails, render the login page
    context = get_context()
    return render_template('login.html', error=error, **context)

# Страница выхода
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('cart', None) # Clear cart on logout as well
    session.pop('visited', None) # Optional: reset visited status
    return redirect(url_for('home'))

# Страница профиля пользователя
@app.route('/profile')
def profile():
    context = get_context()
    if not context['username']:
        # Если пользователь не вошел в систему, перенаправляем на страницу входа
        return redirect(url_for('login'))
    return render_template('profile.html', **context)

# Страница каталога
@app.route('/catalog')
def catalog():
    context = get_context()
    # Передаем товары в шаблон каталога
    return render_template('catalog.html', products=products_db.values(), **context)

# Страница "О нас"
@app.route('/about')
def about():
    context = get_context()
    return render_template('about.html', **context)

# Страница "Частые вопросы"
@app.route('/faq')
def faq():
    context = get_context()
    return render_template('faq.html', **context)

# Добавление товара в корзину (AJAX)
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    if product_id in products_db:
        # Добавляем ID товара в корзину сессии
        # В реальном приложении можно хранить больше деталей или количество
        if product_id not in session['cart']: # Простой пример: не добавлять дубликаты
             session['cart'].append(product_id)
             session.modified = True # Убедиться, что сессия сохраняется
        
        # Возвращаем текущее количество товаров в корзине
        return jsonify({'cartItemsCount': len(session['cart'])})
    return jsonify({'error': 'Product not found'}), 404


# Страница корзины (пока заглушка)
@app.route('/cart')
def cart():
    context = get_context()
    # Получаем детали товаров в корзине
    cart_product_details = [products_db[item_id] for item_id in session.get('cart', []) if item_id in products_db]
    return render_template('cart.html', cart_products=cart_product_details, **context)


if __name__ == '__main__':
    app.run(debug=True)
