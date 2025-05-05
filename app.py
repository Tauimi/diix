from flask import Flask, render_template, request, redirect, url_for, session
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Для использования сессий

# Временная база данных пользователей
users_db = {}

# Счетчик посещений
visitor_count = 0

# Главная страница
@app.route('/')
def home():
    global visitor_count
    if 'visited' not in session:
        # Если пользователь не посещал сайт ранее, увеличиваем счетчик
        visitor_count += 1
        session['visited'] = True  # Помечаем, что пользователь посетил сайт
    return render_template('index.html', username=session.get('username'), visitor_count=visitor_count)

# Страница регистрации
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in users_db:
        return 'Пользователь уже существует.'
    
    # Сохраняем пользователя с хешированием пароля
    users_db[username] = hashlib.sha256(password.encode()).hexdigest()
    session['username'] = username  # Сохраняем пользователя в сессии
    return redirect(url_for('home'))

# Страница входа
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Проверка, если пользователь существует
    if username not in users_db:
        return 'Пользователь не найден.'
    
    # Проверка пароля
    if users_db[username] == hashlib.sha256(password.encode()).hexdigest():
        session['username'] = username  # Сохраняем пользователя в сессии
        return redirect(url_for('home'))
    else:
        return 'Неверный пароль.'

# Страница выхода
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
