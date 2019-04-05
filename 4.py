# 4. Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный
# символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до
# 'f' включительно.

import random

begin = int(input("Input begin int: "))
end = int(input("Input end int: "))

print(random.randint(begin, end))

begin = float(input("Input begin float: "))
end = float(input("Input end float: "))

print(random.uniform(begin, end))

begin = input("Input begin symbol: ")
end = input("Input end symbol: ")

print(chr(random.randint(ord(begin), ord(end))))
