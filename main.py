from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join([
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ])


@app.route('/image_mars')
def image_mars():
    return open('static/html/image_mars.txt', 'r', encoding='utf8').read()


@app.route('/promotion_image')
def promotion_image():
    return open('static/html/promotion_image.txt', 'r', encoding='utf8').read()


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return open('static/html/astronaut_selection.txt', 'r',
                    encoding='utf8').read()
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        print(request.form.getlist('profession'))
        print(request.form.get('sex'))
        print(request.form.get('about'))
        print(request.files['file'].read().decode('utf-8'))
        print(request.form.get('accept'))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return open('static/html/choice.txt', 'r',
                encoding='utf8').read().format(planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return open('static/html/results.txt', 'r',
                encoding='utf8').read().format(nickname, level, rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
