def enter_digit(text):
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
