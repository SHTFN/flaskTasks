from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/users').json(), 'get users')

print(get('http://127.0.0.1:8080/api/users/2').json(), 'get user')

print(post('http://127.0.0.1:8080/api/users', json={
    'name': 'Test add user',
    'surname': 'Test',
    'age': 50,
    'email': 'test@email.com',
    'address': 'Moscow',
    'position': 'Position',
    'speciality': 'Speciality',
    'about': 'about'
}).json(), 'add user')

print(post('http://127.0.0.1:8080/api/users/13', json={
    'name': 'Test_edit_user',
    'surname': 'Test2',
    'age': 60,
    'email': 'test2@email.com',
    'address': 'Saint-Petersburg',
    'position': 'Position',
    'speciality': 'Speciality',
    'about': 'about'
}).json(), 'edit user')

print(delete('http://127.0.0.1:8080/api/users/7').json(), 'delete_user')

