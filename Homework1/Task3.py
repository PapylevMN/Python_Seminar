def enter_digit(text):
    while True:
        flag_negative_digit = False
        dig = input(text)
        if dig.startswith('-'):
            dig = dig[1:]
            flag_negative_digit = True
        if dig.count('.') == 1:
            dig_float = dig[:dig.find('.')] + dig[dig.find('.')+1:]
            if dig_float.isdigit():
                break
            else:
                print('Введенный символ не число! Повторите ввод.')    
        if dig.isdigit():
           break
        else:
            print('Введенный символ не число! Повторите ввод.')
    if flag_negative_digit:
        return -float(dig)
    else:
        return float(dig)

x, y = enter_digit('Введите координату X : '), enter_digit('Введите координату Y : ')
if x > 0 and y > 0:
    print('Точка в 1 четверти')
elif x < 0 and y > 0:
    print('Точка в 2 четверти')
elif x < 0 and y < 0:
    print('Точка в 3 четверти')
elif x > 0 and y < 0:
    print('Точка в 4 четверти')
elif x == 0:
    print('Точка на оси Х')
elif y == 0:
    print('Точка на оси Y')