
from my_library import enter_digit
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
