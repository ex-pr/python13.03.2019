# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import pprint


n = 5
m = 4
a = []
for i in range(n):
    row = input('Введите строку. 4 элемента через пробел: ').split(' ')
    s = 0
    for j in range(len(row)):
        row[j] = int(row[j])
        s += row[j]
    row.append(s)
    a.append(row)

print('Последний столбец матрицы - сумма элементов каждой строки: ')
pprint.pprint(a)



# n = int(input())
# a = [[int(j) for j in input().split(' ')] for i in range(n)]

# M = 4
# N = 5
# a = []
# for i in range(N):
#     b = []
#     s = 0
#     print("%d-я строка:" % i)
#     for j in range(M):
#         n = int(input())
#         s += n
#         b.append(n)
#     b.append(s)
#     a.append(b)
#
# pprint.pprint(a)