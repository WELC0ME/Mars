from flask import Flask

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
