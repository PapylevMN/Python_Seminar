from my_library import enter_digit
result = []
number = int(enter_digit('Введите число : '))
for i in range(1, number+1):
    element = 1
    for j in range (1, i+1):
        element *= j
    result.append(element)
print(*result)