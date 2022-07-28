# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import my_library as ml
nums = ml.random_array()
print(*nums)
print([nums[i]*nums[len(nums)-1-i] for i in range(len(nums)//2 + len(nums)%2)])