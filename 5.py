# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится
# букв.


a = input('Введите букву: ')
b = input('Введите ещё одну букву: ')

print("Номера букв в алфавите: ", ord(a) - 96, ord(b) - 96)
print("Количество букв между ними: ", ord(b) - ord(a) - 1)

# import string

# letter_one = input("Input letter 1: ").lower()
# letter_two = input("Input letter 2: ").lower()
#
# first = string.ascii_lowercase.index(letter_one)
# second = string.ascii_lowercase.index(letter_two)
# print(letter_one, first)
# print(letter_two, second)
#
# print("How many letters:",second - first - 1)
