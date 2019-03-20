# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a = int(input('Введите номер буквы: ')) + 96

print('Под этим номером в алфавите находится буква : ', chr(a))

# import string
#
# letter = input("Input letter 1: ")
#
# print(string.ascii_lowercase.index(letter) + 1)
