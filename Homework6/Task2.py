# 2- Найти сумму чисел списка стоящих на нечетной позиции

from functools import reduce
import my_library as ml
array = ml.random_array()
print(*array)
print(reduce(lambda a,b: a+b, map(lambda x: x[1], (filter(lambda x: x[0]%2 != 0, enumerate(array))))))
print(sum([elem[1] for elem in (filter(lambda x: x[0]%2 != 0, enumerate(array)))]))