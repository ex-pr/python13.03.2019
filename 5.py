# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

a = []

for i in range(random.randint(5,20)):
    a.append(random.randint(-100, 0))
print('Искходный массив: ', a)

max_a = a[0]


for i in range(len(a)):
    if a[i] >= max_a:
        max_a = a[i]

print('Максимальное значение: ', max_a, ', его позиция в массиве: ', a.index(max_a))
