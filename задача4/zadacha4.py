# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random
some_list = [random.randint(1, 10) for _ in range (10)]
print(some_list)
some_set = set(some_list)
print(len(some_set))