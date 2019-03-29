# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import pprint
import random



matr = []

for i in range(5):
    row = []
    for j in range(10):
        row.append(random.randint(1, 100))
    matr.append(row)

pprint.pprint(matr)


mx = 0
c = []
for j in range(10):
    mn = 101
    for i in range(5):
        if matr[i][j] < mn:
            mn = matr[i][j]
    c.append(mn)
    if mn > mx:
        mx = mn

print('Максимальные элементы каждого столбца: ', c)
print("Максимальный среди минимальных: ", mx)


