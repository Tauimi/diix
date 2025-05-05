
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Настройки сессий
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'supersecretkey'
Session(app)

# Данные о товарах (пример)
products = [
    {'id': 1, 'name': 'Телевизор', 'price': 30000, 'description': 'Большой экран 4K'},
    {'id': 2, 'name': 'Холодильник', 'price': 25000, 'description': 'Энергосберегающий'},
    {'id': 3, 'name': 'Стиральная машина', 'price': 20000, 'description': 'Автоматическая'}
]

# Страница главная
@app.route('/')
def home():
    if 'visitor_count' not in session:
        session['visitor_count'] = 0
    session['visitor_count'] += 1
    return render_template('index.html', visitor_count=session['visitor_count'], products=products)

# Страница каталога с фильтрацией и сортировкой
@app.route('/catalog', methods=['GET'])
def catalog():
    sort_order = request.args.get('sort', 'price_asc')

    if sort_order == 'price_asc':
        sorted_products = sorted(products, key=lambda x: x['price'])
    elif sort_order == 'price_desc':
        sorted_products = sorted(products, key=lambda x: x['price'], reverse=True)
    else:
        sorted_products = products

    # Получаем товары из корзины, если они есть
    cart_items = session.get('cart', [])
    return render_template('catalog.html', products=sorted_products, cart_items=cart_items)

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

if __name__ == '__main__':
    app.run(debug=True)
