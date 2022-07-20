def simple():
    sn = [2, 3, 5, 7, 11]
    for n in range(12, 200):
        flag = True
        for i in range(2,n):
            if n % i == 0:
                flag = False
                break
        if flag:
            sn.append(n)
    return sn

import my_library as ml
num = int(ml.enter_digit('Введите число : '))
if num < 0:
    num *=-1
simple_n = simple()
res = []
while num not in simple_n:
    for i in simple_n:
        if num % i == 0:
            res.append(i)
            num /= i
            break
res.append(int(num))
print(f'Список простых множителей : {res}')
