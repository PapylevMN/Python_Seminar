# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from functools import reduce
p1 = list(map(int, input('Введите координаты первой точки: ').split()))
p2 = list(map(int, input('Введите координаты второй точки: ').split()))
d = reduce(lambda a, b: (a + b)**(1/2),(map(lambda p: (p[1] - p[0])**2, zip(p1, p2))))
print(f'Расстояние = {round(d,2)}')

