from data import db_session
from data.jobs import Jobs
from data.users import User
from data.category import Category
import datetime


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Horner'
    user.name = 'Matt'
    user.age = 27
    user.position = 'assistant'
    user.speciality = 'navigator'
    user.address = 'module_2'
    user.email = 'matt@mail.ru'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Reynor'
    user.name = 'Jim'
    user.age = 32
    user.position = 'sergeant'
    user.speciality = 'paratrooper'
    user.address = 'module_2'
    user.email = 'jimmi@rambler.ru'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Li'
    user.name = 'Evan'
    user.age = 22
    user.position = 'brigadier'
    user.speciality = 'pilot'
    user.address = 'module_3'
    user.email = 'pilots@io.org'
    db_sess.add(user)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '1, 2'
    job.start_date = datetime.datetime.now()
    job.is_finished = 0
    db_sess.add(job)
    db_sess.commit()

    category_01 = Category()
    category_01.name = '1'
    db_sess.add(category_01)
    db_sess.commit()

    category_02 = Category()
    category_02.name = '2'
    db_sess.add(category_02)
    db_sess.commit()

    category_03 = Category()
    category_03.name = '3'
    db_sess.add(category_03)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 2
    job.job = 'relax'
    job.work_size = 3
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = 0
    job.categories.append(category_01)
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'repair ship'
    job.work_size = 40
    job.collaborators = '1, 2'
    job.start_date = datetime.datetime.now()
    job.is_finished = 1
    job.categories.append(category_02)
    job.categories.append(category_03)
    db_sess.add(job)
    db_sess.commit()
