# Задана натуральная степень n. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени n.
# *Пример: n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
n = int(input())
k = [random.randint(1,10)]
for i in range(1,n+1):
    k.append(random.randint(0,3))
print(k)
i = 0
st = len(k)-1
res = []
for elem in k:
    res.append(str(elem) + '*x^' + str(st))
    st-=1
for i in range(len(res)-1,-1,-1):
    if res[i].startswith('0'):
        del res[i]
    elif res[i].startswith('1'):
        res[i] = res[i][2:]
for i in range(len(res)):
    if res[i][-1] == '1':
        res[i] = res[i][:-2]
    elif res[i][-1] == '0':
        res[i] = res[i][:-4]

s = ' + '.join(res) + ' = 0'
print(s)
with open('data.txt', 'w', encoding='utf-8') as file:
    print(s, file = file)