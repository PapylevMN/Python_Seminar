# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
import my_library as ml
n = int(ml.enter_digit('Введите количество членов последовательности :'))
print(*[(-3)**i for i in range(n)])