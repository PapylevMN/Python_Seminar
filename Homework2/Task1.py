from my_library import enter_digit

number = enter_digit('Введите число : ')
if number < 0:
    number *= -1
number = int(str(number).replace('.', ''))
sum = 0
while number > 0:
    sum = sum + number % 10
    number = number // 10
print(f'Сума цифр в числе = {sum}')
