# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


a = []
for i in range(10):
    a.append(random.randint(0, 49))

print(a)



def merge_part(a):
    def merge(a, b):
        result = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        result += a[i:] + b[j:]
        return result

    if len(a) <= 1:
        return a
    else:
        c = a[:len(a)//2]
        d = a[len(a)//2:]
        return merge(merge_part(c), merge_part(d))

print(merge_part(a))
