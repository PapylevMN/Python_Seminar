from my_library import enter_digit
result = {}
number = int(enter_digit('Введите число : '))
if number < 0:
    number *= -1
for i in range(1, number+1):
    result[i] = round((1+1/i)**i,3)
print(result)