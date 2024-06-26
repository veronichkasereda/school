from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('base.html', title='Обо мне')


@app.route('/about')
def about():
    return render_template('about.html', title='О себе')


@app.route('/galery', methods=['GET'])
def galery():
    if request.method == 'GET':
        return render_template('galery.html',
                               title='Галерея')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты')


@app.route('/recommend')
def recommend():
    return render_template('recommend.html', title='Полезные советы')


@app.route('/form', methods=["GET", "POST"])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    save_text(name, email)
    return render_template('form.html', title='Форма обратной связи')


def save_text(name, email):
    print(name, email)


# механизм  сохранения данных о пользоваетлях находится в разработке, но может выглядеть так
#    with open('form.txt') as file:
#        file.write(f'{name}, контактные данные: {email}')
#        print(file.read())


if __name__ == '__main__':
    app.run()
