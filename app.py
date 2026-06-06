"""
Соцветие — сайт цветочного магазина.
Учебный проект для портфолио.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key')

# Данные о букетах (в реальном проекте было бы в базе данных)
BOUQUETS = [
    {
        'id': 1,
        'name': 'Утренний туман',
        'description': 'Роза кремовая, гортензия голубая, хризантема кустовая белая, эвкалипт',
        'price': 3500,
        'image': 'bouquet-1.jpg',
        'tag': 'Хит продаж'
    },
    {
        'id': 2,
        'name': 'Карамельная осень',
        'description': 'Роза персиковая, пион белый, рускус, сухоцветы, корзина из лозы',
        'price': 4200,
        'image': 'bouquet-2.jpg',
        'tag': 'Новинка'
    },
    {
        'id': 3,
        'name': 'Сладкие сны',
        'description': 'Роза розовая, хризантема жёлтая, астры белые, пастельная роза',
        'price': 3200,
        'image': 'bouquet-3.jpg',
        'tag': 'Сезонное'
    },
    {
        'id': 4,
        'name': 'Пряный вечер',
        'description': 'Роза персиковая, гвоздика белая, папоротник, сухоцветы',
        'price': 3800,
        'image': 'bouquet-4.jpg',
        'tag': 'Популярное'
    },
    {
        'id': 5,
        'name': 'Перламутр',
        'description': 'Хризантема розовая и белая, эустома лиловая, лаванда, декоративные ягоды',
        'price': 4500,
        'image': 'bouquet-5.jpg',
        'tag': 'Хит продаж'
    },
    {
        'id': 6,
        'name': 'Ягодный бархат',
        'description': 'Роза белая и персиковая, эвкалипт, гиперикум, брассика, астильба',
        'price': 5500,
        'image': 'bouquet-6.jpg',
        'tag': 'Премиум'
    },
]


@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html', bouquets=BOUQUETS[:4])


@app.route('/catalog/')
def catalog():
    """Каталог букетов"""
    return render_template('catalog.html', bouquets=BOUQUETS)


@app.route('/about/')
def about():
    """О магазине"""
    return render_template('about.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    """Контакты и форма обратной связи (демо)"""
    if request.method == 'POST':
        # Данные НЕ сохраняются и НЕ выводятся — это учебный проект
        flash(
            'Спасибо! Это демонстрационная форма. Ваши данные не были сохранены.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/bouquet/<int:bouquet_id>/')
def bouquet_detail(bouquet_id):
    """Детальная страница букета (опционально)"""
    bouquet = next((b for b in BOUQUETS if b['id'] == bouquet_id), None)
    if bouquet:
        return render_template('detail.html', bouquet=bouquet)
    return redirect(url_for('catalog'))


# Контекстный процессор — добавляет информацию во все шаблоны
@app.context_processor
def inject_globals():
    return {
        'shop_name': 'Соцветие',
        'shop_tagline': 'авторские букеты',
        'phone': '+7 (999) 123-45-67',
        'email': 'hello@bloom-flowers.ru',
        'address': 'ул. Цветочная, 15, Москва',
        'is_portfolio': True,
    }


if __name__ == '__main__':
    app.run(debug=True)
