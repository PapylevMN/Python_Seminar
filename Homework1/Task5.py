from my_library import enter_digit

print('Введите координаты точки А:')
x,y = enter_digit('X - > '), enter_digit('Y - > ')
print('Введите координаты точки B:')
x1,y1 = enter_digit('X - > '), enter_digit('Y - > ')
distance = ((x1-x)**2 + (y1-y)**2)**(1/2)
print(round(distance,2))
