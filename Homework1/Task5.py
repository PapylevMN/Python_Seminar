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
        if dig.isdigit():
           break
        else:
            print('Введенный символ не число! Повторите ввод.')
    if flag_negative_digit:
        return -float(dig)
    else:
        return float(dig)

print('Введите координаты точки А:')
x,y = enter_digit('X - > '), enter_digit('Y - > ')
print('Введите координаты точки B:')
x1,y1 = enter_digit('X - > '), enter_digit('Y - > ')
distance = ((x1-x)**2 + (y1-y)**2)**(1/2)
print(round(distance,2))
