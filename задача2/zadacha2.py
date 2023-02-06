# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

print('введи количество')
N = int(input())
dict_list = []
for _ in range(N):
    name = input()
    age = int(input())
    dict_list.append({'name': name, 'age': age})
print(dict_list)
min_age = dict_list[0]['age']
for some_dict in dict_list:
    if some_dict['age'] < min_age:
        min_age = some_dict['age']
for some_dict in dict_list:
    if some_dict['age'] == min_age:
        print(some_dict['name'])
        break