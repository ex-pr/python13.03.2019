# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


a = input('Введите натруальные числа через запятую: ').split(',')

max = 0

lst = {}
for i in a:
    sum = 0
    for m in i:
        sum += int(m)
        lst[i] = sum


for i in lst:
    print("'%s':%d" % (i, lst[i]))

for key in lst:
    if max < lst[key]:
        max = lst[key]

def get_key(lst, value):
    for k, v in lst.items():
        if v == value:
            return k

print('Самая большая сумма цифр у числа: ', get_key(lst, max), '. Сумма цифр равна: ', b)


