# 4. Определить, какое число в массиве встречается чаще всего.

a = [1, 45, 38, 90, -54, -54, 80, -54]


b = {}

def mycount(a):
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    return b


def get_key(lst, value):
    for k, v in lst.items():
        if v == value:
            return k


mycount(a)


for i in b:
    print("'%s':%d" % (i, b[i]))


c = 0

for i in b:
    if b[i] > c:
        c = b[i]

d = get_key(b, c)

print("Наибольшее количество встречается число'%s': %d раз" % (d, c))