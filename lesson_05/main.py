from flask import Flask, render_template, redirect, abort, request
from data import db_session
from data.jobs import Jobs
from data.users import User
from data.departments import Departments
from forms.loginform import LoginForm
from forms.jobform import JobForm
from forms.registerform import RegisterForm
from forms.departmentform import DepartmentForm
from flask import make_response, jsonify
from flask_login import (LoginManager, logout_user, login_required, login_user,
                         current_user)
from flask_restful import Api
from requests import get
from PIL import Image
import os
from api import users_resource, job_resource


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ChtobiVamBuloSlojneeZaponitGitMuPobedim'
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def works_log():
    db_sess = db_session.create_session()
    return render_template("works_log.html", jobs=db_sess.query(Jobs).all())


@app.route('/departments')
def departments():
    db_sess = db_session.create_session()
    return render_template("departments.html",
                           departments=db_sess.query(Departments).all())


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@login_required
@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
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
        return redirect('/')
    return render_template('add_job.html', title='Добавление работы',
                           form=form)


@login_required
@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = Departments(
            title=form.title.data,
            chief=form.chief_id.data,
            members=form.members.data,
            email=form.email.data,
        )
        db_sess.add(department)
        db_sess.commit()
        return redirect('/departments')
    return render_template('add_department.html',
                           title='Добавление департамента', form=form)


@login_required
@app.route('/edit_job/<int:id_>', methods=['GET', 'POST'])
def edit_job(id_):
    form = JobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id_).first()
        if job:
            form.job_title.data = job.job
            form.team_leader_id.data = job.team_leader
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id_).first()
        if job:
            job.team_leader = form.team_leader_id.data
            job.job = form.job_title.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job.html', title='Редактирование работы',
                           form=form)


@login_required
@app.route('/edit_department/<int:id_>', methods=['GET', 'POST'])
def edit_department(id_):
    form = DepartmentForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        department = db_sess.query(Departments).filter(
            Departments.id == id_).first()
        if department:
            form.title.data = department.title
            form.chief_id.data = department.chief
            form.members.data = department.members
            form.email.data = department.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = db_sess.query(Departments).filter(
            Departments.id == id_).first()
        if department:
            department.title = form.title.data
            department.chief = form.chief_id.data
            department.members = form.members.data
            department.email = form.email.data
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('add_department.html',
                           title='Редактирование департамента', form=form)


@login_required
@app.route('/remove_job/<int:id_>', methods=['GET', 'POST'])
def remove_job(id_):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id_).first()
    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@login_required
@app.route('/remove_department/<int:id_>', methods=['GET', 'POST'])
def remove_department(id_):
    db_sess = db_session.create_session()
    department = db_sess.query(Departments).filter(
        Departments.id == id_).first()
    if department:
        db_sess.delete(department)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


@app.route('/users_show/<int:user_id>', methods=['GET'])
def users_show(user_id):

    def get_map_params(obj):
        lower_corner = obj["boundedBy"]["Envelope"]["lowerCorner"].split()
        upper_corner = obj["boundedBy"]["Envelope"]["upperCorner"].split()
        pos = obj["Point"]["pos"]
        longitude, lattitude = pos.split(" ")
        return {
            "ll": ",".join([longitude, lattitude]),
            "spn": ",".join([
                str((float(upper_corner[0]) - float(lower_corner[0])) / 2),
                str((float(upper_corner[1]) - float(lower_corner[1])) / 2)
            ]),
            "l": "sat"
        }

    user = get('http://127.0.0.1:8080/api/users/' + str(user_id)).json()[
        'users']
    if 'error' in list(user.keys()):
        params = {
            'title': 'Nostalgy',
            'error': user['error']
        }
    else:
        try:
            response = get("http://geocode-maps.yandex.ru/1.x/", params={
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": user['city_from'],
                "format": "json"
            }).json()
            response = get("http://static-maps.yandex.ru/1.x/",
                           params=get_map_params(
                               response["response"]["GeoObjectCollection"][
                                   "featureMember"][0]["GeoObject"]))
            number = len(os.listdir('static/temp'))
            with open('static/temp/' + str(number) + '.png', "wb") as file:
                file.write(response.content)
            hint = ''
        except Exception:
            img = Image.new((100, 100), 'RGB', (128, 128, 128))
            img.save('static/temp/map.png')
            hint = 'City not found'
        params = {
            'title': 'Nostalgy',
            'name': user['name'],
            'surname': user['surname'],
            'city': user['city_from'],
            'image': number,
            'hint': hint,
        }
    return render_template('users_show.html', **params)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    api.add_resource(users_resource.UserResource,
                     '/api/v2/users/<int:user_id>')
    api.add_resource(users_resource.UserListResource, '/api/v2/users')
    api.add_resource(job_resource.JobResource, '/api/v2/jobs/<int:job_id>')
    api.add_resource(job_resource.JobListResource, '/api/v2/jobs')
    app.run(port=8080, host='127.0.0.1')
