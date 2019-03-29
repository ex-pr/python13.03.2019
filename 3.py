# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = []

for i in range(random.randint(5,20)):
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
a[imin],a[imax] = a[imax],a[imin]

print(a)

# min_a = min(a)
# max_a = max(a)
# imin = a.index(min_a)
# imax = a.index(max_a)
# a[imin],a[imax] = a[imax],a[imin]
# print(min_a, max_a, imin, imax)


