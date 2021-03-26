from requests import get, post, delete, put

# -----------------------------------------------------------------------------
print('--------------------------JOBS----------------------------------------')
print(get('http://localhost:8080/api/v2/jobs').json())
print(get('http://localhost:8080/api/v2/jobs/3').json())
print(get('http://localhost:8080/api/v2/jobs/999').json())
print(get('http://localhost:8080/api/v2/jobs/hello_world').json())
# -----------------------------------------------------------------------------
# POST-запрос без json
print(post('http://localhost:8080/api/v2/jobs').json())
# POST-запрос с неполным json
print(post('http://localhost:8080/api/v2/jobs',
           json={
               'team_leader': 2,
           }).json())
# POST-запрос, но такое ID уже существует
print(post('http://localhost:8080/api/v2/jobs',
           json={
               'id': 6,
               'team_leader': 1,
               'job': 'Test job',
               'work_size': 20,
               'collaborators': '1, 2, 4',
               'is_finished': True,
           }).json())
# корректный POST-запрос
print(post('http://localhost:8080/api/v2/jobs',
           json={
               'id': 7,
               'team_leader': 1,
               'job': 'Test job',
               'work_size': 20,
               'collaborators': '1, 2, 4',
               'is_finished': True,
           }).json())
# проверяем, что работа добавилась
print(get('http://localhost:8080/api/v2/jobs').json())
# -----------------------------------------------------------------------------
# добавляем работу
print(post('http://localhost:8080/api/v2/jobs',
           json={
               'id': 8,
               'team_leader': 1,
               'job': 'Test job',
               'work_size': 20,
               'collaborators': '1, 2, 4',
               'is_finished': True,
           }).json())
# пытаемся удалить несуществующую работу
print(delete('http://localhost:8080/api/v2/jobs/999').json())
# пытаемся выполнить неккоректный запрос(строка)
print(delete('http://localhost:8080/api/v2/jobs/hello_world').json())
# удаляем работу
print(delete('http://localhost:8080/api/v2/jobs/8').json())
# проверяем, что все удалилось
print(get('http://localhost:8080/api/v2/jobs').json())
# -----------------------------------------------------------------------------
# добавляем работу
print(post('http://localhost:8080/api/v2/jobs',
           json={
               'id': 8,
               'team_leader': 1,
               'job': 'Test job',
               'work_size': 20,
               'collaborators': '1, 2, 4',
               'is_finished': True,
           }).json())
# пытаемся выполнить запрос без json
print(put('http://localhost:8080/api/v2/jobs/2').json())
# пытаемся выполнить запрос c некорректным json
print(put('http://localhost:8080/api/v2/jobs/2',
          json={
              'something': 12,
          }).json())
# пытаемся изменить несуществующую работу
print(put('http://localhost:8080/api/v2/jobs/999',
          json={
              'team_leader': 2,
          }).json())
# меняем описание работы
print(put('http://localhost:8080/api/v2/jobs/2',
          json={
              'job': 'Edited test job',
          }).json())
# проверяем изменения
print(get('http://localhost:8080/api/v2/jobs').json())
# -----------------------------------------------------------------------------
print('-------------------------USERS----------------------------------------')
print(get('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/3').json())
print(get('http://localhost:8080/api/v2/users/999').json())
print(get('http://localhost:8080/api/v2/users/hello_world').json())
# -----------------------------------------------------------------------------
# POST-запрос без json
print(post('http://localhost:8080/apiv2//users').json())
# POST-запрос с неполным json
print(post('http://localhost:8080/api/v2/users',
           json={
               'name': 'David',
               'age': 21
           }).json())
# POST-запрос, но такое ID уже существует
print(post('http://localhost:8080/api/v2/users',
           json={
               'id': 6,
               'surname': 'Black',
               'name': 'David',
               'age': 21,
               'position': 'capitan',
               'speciality': 'engineer',
               'address': 'module 1',
               'email': 'DavidBlack@mars.com',
               'password': 'CoolDavid2000',
           }).json())
# корректный POST-запрос
print(post('http://localhost:8080/api/v2/users',
           json={
               'id': 7,
               'surname': 'Black',
               'name': 'David',
               'age': 21,
               'position': 'capitan',
               'speciality': 'engineer',
               'address': 'module 1',
               'email': 'DavidBlackCapitan@mars.com',
               'password': 'CoolDavid2000',
           }).json())
# проверяем, что пользователь добавился
print(get('http://localhost:8080/api/v2/users').json())
# -----------------------------------------------------------------------------
# добавляем пользователя
print(post('http://localhost:8080/api/v2/users',
           json={
               'id': 9,
               'surname': 'Li',
               'name': 'Oliver',
               'age': 43,
               'position': 'assistant',
               'speciality': 'engineer',
               'address': 'module 1',
               'email': 'oliverLi2@help.com',
               'password': 'oliver78',
           }).json())
# пытаемся удалить несуществующего пользователя
print(delete('http://localhost:8080/api/v2/users/999').json())
# пытаемся выполнить неккоректный запрос(строка)
print(delete('http://localhost:8080/api/v2/users/hello_world').json())
# удаляем пользователя
print(delete('http://localhost:8080/api/v2/users/9').json())
# проверяем, что все удалилось
print(get('http://localhost:8080/api/v2/users').json())
# -----------------------------------------------------------------------------
# добавляем пользователя
print(post('http://localhost:8080/api/v2/users',
           json={
               'id': 10,
               'surname': 'Li',
               'name': 'Oliver',
               'age': 43,
               'position': 'assistant',
               'speciality': 'engineer',
               'address': 'module 1',
               'email': 'oliverLi2@help.com',
               'password': 'oliver78',
           }).json())
# пытаемся выполнить запрос без json
print(put('http://localhost:8080/api/v2/users/2').json())
# пытаемся выполнить запрос c некорректным json
print(put('http://localhost:8080/api/v2/users/2',
          json={
              'something': 12,
          }).json())
# пытаемся изменить несуществующего пользователя
print(put('http://localhost:8080/api/v2/users/999',
          json={
              'address': 'module 2',
          }).json())
# меняем адрес пользователя
print(put('http://localhost:8080/api/v2/users/2',
          json={
              'address': 'module 2',
          }).json())
# проверяем изменения
print(get('http://localhost:8080/api/v2/users').json())
# -----------------------------------------------------------------------------

input()
