# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

a = []

for i in range(6):
    a.append(random.randint(-100, 100))


print('Исходный массив: ', a)


min_one = a[0]

for i in range(len(a)):
    if a[i] <= min_one:
        min_one = a[i]

a.remove(min_one)


min_two = a[0]

for j in range(len(a)):
    if a[j] < min_two:
        min_two = a[j]

print('Два минимальных числа: ', min_one, min_two)