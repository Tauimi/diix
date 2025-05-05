
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Настройки сессий
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'supersecretkey'
Session(app)

# Данные о товарах (пример)
products = [
    {'id': 1, 'name': 'Телевизор', 'price': 30000, 'description': 'Большой экран 4K', 'category': 'tv'},
    {'id': 2, 'name': 'Холодильник', 'price': 25000, 'description': 'Энергосберегающий', 'category': 'fridge'},
    {'id': 3, 'name': 'Стиральная машина', 'price': 20000, 'description': 'Автоматическая', 'category': 'washing_machine'}
]

# Данные о новостях (пример)
news = [
    {'title': 'Большая скидка на телевизоры!', 'content': 'Успейте приобрести телевизоры со скидкой 20%! Только до конца месяца.'},
    {'title': 'Новый холодильник с функцией No Frost!', 'content': 'Представляем новый холодильник с уникальной функцией No Frost. Покупай сейчас!'},
    {'title': 'Стиральные машины с дополнительными функциями', 'content': 'Обновленный ассортимент стиральных машин с новыми функциями и более высоким классом энергосбережения.'}
]

# Страница главная
@app.route('/')
def home():
    if 'visitor_count' not in session:
        session['visitor_count'] = 0
    session['visitor_count'] += 1
    return render_template('index.html', visitor_count=session['visitor_count'], products=products, news=news)

# Страница каталога с фильтрацией и сортировкой
@app.route('/catalog', methods=['GET'])
def catalog():
    category = request.args.get('category', 'all')
    sort_order = request.args.get('sort', 'price_asc')
    search_query = request.args.get('search', '')

    filtered_products = products

    # Фильтрация по категории
    if category != 'all':
        filtered_products = [prod for prod in products if category in prod['category']]

    # Фильтрация по поисковому запросу
    if search_query:
        filtered_products = [prod for prod in filtered_products if search_query.lower() in prod['name'].lower()]

    # Сортировка
    if sort_order == 'price_asc':
        filtered_products = sorted(filtered_products, key=lambda x: x['price'])
    elif sort_order == 'price_desc':
        filtered_products = sorted(filtered_products, key=lambda x: x['price'], reverse=True)
    elif sort_order == 'name_asc':
        filtered_products = sorted(filtered_products, key=lambda x: x['name'])
    elif sort_order == 'name_desc':
        filtered_products = sorted(filtered_products, key=lambda x: x['name'], reverse=True)

    cart_items = session.get('cart', [])
    return render_template('catalog.html', products=filtered_products, cart_items=cart_items, search_query=search_query)

# Страница товара
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    return render_template('product_detail.html', product=product)

# Добавить товар в корзину
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('catalog'))

# Удалить товар из корзины
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item != product_id]
    session['cart'] = cart
    return redirect(url_for('cart'))

# Страница корзины покупок
@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    cart_products = [next(prod for prod in products if prod['id'] == item_id) for item_id in cart_items]
    return render_template('cart.html', cart_products=cart_products)

# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['user'] = username
        return redirect(url_for('home'))
    return render_template('login.html')

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Страница "Частые вопросы"
@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
