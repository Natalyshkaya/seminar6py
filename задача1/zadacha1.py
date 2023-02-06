# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. 
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение

print('введи количество')
count = int(input())
fruit_dict = {}
for _ in range(count):
    fruit = input()
    count_fruits = int(input())
    fruit_dict[fruit] = count_fruits
print(fruit_dict)