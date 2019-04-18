# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# # промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# # в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random


def bubble(a):
    n = 1
    while n < len(a):
        for j in range(len(a) - n):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        n += 1
    return a



def bubble_optimized(a):
    j = len (a) - 1
    not_ordered= True
    while not_ordered:
        not_ordered = False
        for k in range(0, j):
            if a[k] < a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                not_ordered = True
        j -= 1
    return a

a = []
for i in range(10):
    a.append(random.randint(-100, 99))

print(a)
print(bubble(a))
print(bubble_optimized(a))
