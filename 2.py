# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

print('Число 5: ', bin(a))
print('Число 6: ', bin(b))
print('Операция "И": ', a & b, bin(a & b))
print('Операция "ИЛИ": ', a | b, bin(a | b))
print('Побитовый сдвиг влево: ', a>>1, bin(a>>1))
print('Побитовый сдвиг вправо: ', a<<1, bin(a<<1))