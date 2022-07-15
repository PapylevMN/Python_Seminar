
from my_library import enter_digit

def fibonac_pos(num):
    if num in (1,2):
        return 1
    elif num == 0:
        return 0
    return fibonac_pos(num-1) + fibonac_pos(num-2)

def fibonac_neg(num):
    if num in (-1,0):
        return 1
    return (-1) ** (-num-1) * fibonac_pos(-num)

n = int(enter_digit('Введите количество элементов ряда Фибоначчи: '))
if n < 0:
    n *= -1
    print('Количество элементов должно быть положительным. Параметр принят по модулю.')
fibo = []
for i in range(-n,0):
    fibo.append(fibonac_neg(i))

for i in range(0,n+1):
    fibo.append(fibonac_pos(i))
print(fibo)
