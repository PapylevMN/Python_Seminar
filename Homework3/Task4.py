from my_library import enter_digit

def binary_convert_to_negative(bin_number):
    digit = 1
    for i in range(len(bin_number)-1,-1,-1):
        bin_number[i] = not bin_number[i]
        bin_number[i] = int(bin_number[i])
        if bin_number[i] == 0 and digit == 1:
            bin_number[i] = 1
            digit = 0
        elif bin_number[i] == 1 and digit == 1:
            bin_number[i] = 0
            digit = 1
        elif bin_number[i] == 1 and digit == 0:
            bin_number[i] = 1
            digit = 0
        elif bin_number[i] == 0 and digit == 0:
            bin_number[i]  = 0
            digit = 0
    return bin_number

num = int(enter_digit('Введите число: '))
flag_negative = 1
if num < 0:
    flag_negative = -1
    num *= flag_negative

result = []

while num > 1:
     result.append(num%2)
     num = num//2

result.append(num)

for _ in range(24-len(result)):
    result.append(0)

result = result[::-1]

if flag_negative == -1:
    result = binary_convert_to_negative(result)
    print(*result, sep = '')
else:
    print(*result, sep = '')


