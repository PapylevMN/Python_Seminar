
import random
from my_library import enter_digit
array = []
length_array = int(enter_digit('Введите размер массива: '))
if length_array<0:
    length_array *=-1
    print('Введено отрицательное число. Данные взяты по модулю')
for _ in range(length_array):
    array.append(round(random.uniform(1.0, 20.0 ), 3))
print(*array)
array = [round((n-int(n)),3) for n in array]
print(f'Разница между {max(array)} и {min(array)} = {max(array) - min(array)}')