import my_library as ml
d = int(ml.enter_digit('Введите требуемое количество знаков : '))
if d<0:
    d*=-1
dif = 10**(d*-1)
n = 2
sign = 1
sum = 0
pi = 0.141592653589793
while abs(pi - sum) > dif:
    znam = 1
    for i in range(n,n+3):
        znam *= i
    sum += 4*sign/(znam)
    sign *=-1
    n +=2
print(f'Pi = {3+sum} или {round(3+sum, d)}')