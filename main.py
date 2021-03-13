from flask import Flask, render_template, request, redirect
from PIL import Image
import os
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChtobiVamBuloSlojneeZaponitGitMuPobedim'


@app.route('/<title>')
def base(title):
    params = {
        'title': title,
    }
    return render_template('base.html', **params)


@app.route('/index/<title>')
def index(title):
    params = {
        'title': title,
    }
    return render_template('base.html', **params)


@app.route('/training/<prof>')
def training(prof):
    if any([i in prof for i in ['инженер', 'строитель']]):
        heading = 'Инженерные тренажеры'
        image = 'engineer.jpg'
    elif any([i in prof for i in ['ученый', 'программист']]):
        heading = 'Научные симуляторы'
        image = 'scientist.jpg'
    else:
        heading = 'Неизвестно'
        image = 'question.jpg'
    params = {
        'title': 'Mars',
        'heading': heading,
        'image': image,
    }
    return render_template('training.html', **params)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = [
        'Пилот',
        'Строитель',
        'Экзобиолог',
        'Врач',
        'Оператор дронов',
        'Штурман',
        'Киберинженер',
        'Оператор марсохода',
        'Метеоролог',
        'Инженер по терраформированию',
    ]
    params = {
        'title': 'Mars',
        'profs': profs,
        'type': list,
    }
    return render_template('list_prof.html', **params)


@app.route('/distribution')
def distribution():
    people = [
        'Ридли Скотт',
        'Энди Уир',
        'Марк Уотни',
        'Венката Капур',
        'Тедди Сандерс',
        'Шон Бин',
    ]
    params = {
        'title': 'Mars',
        'people': people,
    }
    return render_template('distribution.html', **params)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {
        'title': 'Mars',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True',
    }
    return render_template('auto_answer.html', **params)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    params = {
        'title': 'Mars',
        'sex': sex,
        'age': int(age),
    }
    return render_template('table.html', **params)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        try:
            files = os.listdir('static/images/temp')
            number = str(int(files[-1][:-4]) + 1) if len(files) > 0 else '0'
            Image.open(request.files['file']
                       ).save('static/images/temp/' + number + '.png')
        except Exception as e:
            print(e)
    params = {
        'images': os.listdir('static/images/temp'),
    }
    return render_template('galery.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
