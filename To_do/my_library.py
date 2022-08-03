import random
def random_array():
    array = []
    length_array = int(enter_digit('Введите размер массива: '))
    low = int(enter_digit('Введите нижнюю границу массива: '))
    high = int(enter_digit('Введите верхнюю границу массива: '))
    if length_array < 0:
        length_array *= -1
        print('Введено отрицательное число. Данные взяты по модулю')
    for _ in range(length_array):
        array.append(random.randint(low, high))
    return array

def enter_digit(text:str):
    '''
    Проверяет ввод пользователя на число

    :params: Принимает интерфейс пользователя в виде текстового сообщения

    :return: Возвращает число типа float
    '''
    while True:
        flag_negative_digit = 1
        number = input(text)
        if number.startswith('-'):
            number = number[1:]
            flag_negative_digit = -1
        if number.count('.') == 1:
            number_float = number.replace('.', '')
            if number_float.isdigit():
                break
        if number.isdigit():
            break
        else:
            print('Введенный символ не число! Повторите ввод.')
    return float(number)*flag_negative_digit


def enter_candy(text:str):
    while True:
        number = input(text)
        if number.startswith('-') or number.count('.') == 1:
            print('Число должно быть целое от 1 до 28! Повторите ввод.')
        if number.isdigit() and 0 < int(number) < 29:
            break
        else:
            print('Введенный символ вне диапазона, либо не число! Повторите ввод.')
    return int(number)