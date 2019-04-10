# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


hex_numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

ten_numb = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert(c):
    c_deque = deque(c.upper())
    return c_deque


def summa(first, second):
    first = first.copy()
    second = second.copy()
    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    summ = deque()
    rest = 0
    for i in range(len(first) - 1, -1, -1):
        first_i = ten_numb[first[i]]
        second_i= ten_numb[second[i]]
        result = first_i + second_i + rest

        if result >= 16:
            rest = 1
            result -= 16
        else:
            rest = 0

        summ.appendleft(hex_numb[result])

    if rest == 1:
        summ.appendleft('1')

    return summ


def multpl(first, second):

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()

    for i in range(len(first) - 1, -1, -1):
        second_i = ten_numb[second[i]]
        last = deque()

        for j in range(second_i):
            last = summa(last, first)

        last.extend('0' * (len(first) - i - 1))

        result = summa(result, last)

    return result


a = (input('Введите первое число'))
b = (input('Введите второе число'))

a = convert(a)
b = convert(b)


print("A + B =", summa(a, b))
print("A * B =", multpl(a, b))