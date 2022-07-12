# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#    *Пример:*
# Для N = 5: 1, -3, 9, -27, 81

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
from my_library import enter_digit
dict = {}
n = int(enter_digit('Введите число: '))
for i in range(1, n+1):
    dict[i] = dict.get(i, i*3+1)
print(dict)

n = int(enter_digit('Введите число : -- >'))
res = [int(n) for n in range(n)]
res[0]= 1
for i in range(1,n):
    if i%2 != 0:
        res[i] = res[i-1]*-3
    else:
        res[i] = res[i-2]*9
print(*res)



s_main = input('Введите строку :').lower()
s_sub = input('Введите строку поиска :').lower()
count = 0
ind = s_main.find(s_sub)
while ind != -1:
    count = count + 1
    s_main = s_main[ind+len(s_sub):]
    ind = s_main.find(s_sub)
print(count)
