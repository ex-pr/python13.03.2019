# 1. Определение количества различных подстрок с использованием хэш-функции.
# # Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# # Требуется найти количество различных подстрок в этой строке.


def count_substring(s: str):
    set_str = set()

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            set_str.add(hash(s[i:j]))

    count = len(set_str) - 1
    return count

a = input('Введите строку: ')
count = count_substring(a)
print("В строке {} количество подстрок {}".format(a, count))