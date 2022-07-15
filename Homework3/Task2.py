import random
from my_library import enter_digit
array = []
length_array = int(enter_digit('Введите размер массива: '))
if length_array < 0:
    length_array *= -1
    print('Введено отрицательное число. Данные взяты по модулю')
for _ in range(length_array):
    array.append(random.randint(0, 20))
print(*array)
result_array = []
for i in range(len(array)//2):
    result_array.append(array[i]*array[len(array)-1-i])
if len(array) % 2 != 0:
    result_array.append(array[len(array)//2] ** 2)
print(*result_array)
