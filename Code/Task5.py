"""
Перед вами словарь user
При помощи метода pop переименуйте в нем следующие ключи:
ключ password в ключ secret
ключ last_name в ключ surname

user = {
    "id": 4170,
    "first_name": "Teresa",
    "password": "SyUpfo1ljm",
    "last_name": "Wehner",
    "email": "teresa.wehner@email.com"
}
"""
user = {
    "id": 4170,
    "first_name": "Teresa",
    "password": "SyUpfo1ljm",
    "last_name": "Wehner",
    "email": "teresa.wehner@email.com"
}

pass_ = user.pop('password')
user['secret'] = pass_
last_name = user.pop('last_name')
user.setdefault('surname', last_name)

print(user)


