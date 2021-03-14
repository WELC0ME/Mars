from flask import Flask, render_template, request, redirect
from PIL import Image
import os
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from forms.addjobform import AddJobForm
from data import db_session
from data.jobs import Jobs
from data.users import User
from flask_login import LoginManager, logout_user, login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChtobiVamBuloSlojneeZaponitGitMuPobedim'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


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


@app.route('/member')
def member():
    users = eval(open('templates/members.json', 'r', encoding='utf8').read())
    return render_template('member.html', title='Mars', users=users)


@app.route('/journal')
def journal():
    db_sess = db_session.create_session()
    return render_template("journal.html", jobs=db_sess.query(Jobs).all())


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = AddJobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=form.team_leader_id.data,
            job=form.job_title.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data,
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/journal')
    return render_template('add_job.html', title='Adding a job', form=form)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')
