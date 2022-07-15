import random
from my_library import enter_digit
array = []
length_array = int(enter_digit('Введите размер массива: '))
if length_array < 0:
    length_array *= -1
    print('Введено отрицательное число. Данные взяты по модулю')
for _ in range(length_array):
    array.append(random.randint(0, 100))
print(*array)
sum = 0
for i in range(length_array):
    if i % 2 != 0:
        sum += array[i]
print(f'Сумма элементов, стоящих на нечетных позициях = {sum}')
