# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = []

for i in range(6):
    a.append(random.randint(-100, 100))
print('Исходный массив: ', a)


max_a = a[0]


for i in range(len(a)):
    if a[i] >= max_a:
        max_a = a[i]

print('Максимальное значение: ', max_a)

min_a = a[0]

for j in range(len(a)):
    if a[j] <= min_a:
        min_a = a[j]

print('Минимальное значение: ', min_a)

imin = a.index(min_a)
imax = a.index(max_a)

if imin > imax:
    imax, imin = imin, imax


c = 0
for i in range(imin+1, imax):
    c += a[i]

print(c)