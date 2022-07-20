import my_library as ml
import random
def random_array():
    length = int(ml.enter_digit('Введите размер массива: '))
    print('Введите границы диапазона случайных чисел :')
    low = int(ml.enter_digit('Нижняя ->'))
    flag = True
    while flag:
        high = int(ml.enter_digit('Верхняя ->'))
        if high > low:
            flag = False
        else:
            print('ОШИБКА! Верхняя граница меньше, либо равна нижней! Повторите ввод.')

    array = []
    if length < 0:
        length *= -1

    for _ in range(length):
        array.append(random.randint(low, high))
    return array

array = random_array()
print(array)
non_repeat = {elem: array.count(elem) for elem in array}
result = [k for k in non_repeat.keys() if non_repeat[k] == 1]
print(f'Список неповторяющихся элементов -> {result}')