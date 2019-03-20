# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа
# должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.


def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multip(a, b):
    return a * b

def divis(a, b):
    return a / b

def myexit(a,b):
    exit()

def chs_command():
    for i in menu:
        print(f"{i}")
    command = input('Выберите команду (0 - Для выхода из программы): ')
    return command


menu = {
    "+": plus,
    "-": minus,
    "*": multip,
    "/": divis,
    "0": myexit
}

while True:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    command = chs_command()


    while True:
        if command in menu.keys():
            while command == '/' and b == 0:
                print('Нельзя делить на 0!')
                command = chs_command()
            print('Результат вычислений: ', menu[command](a, b))
            break
        else:
                print('Ввели неверную команду.')
                command = chs_command()













