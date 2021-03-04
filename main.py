from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
