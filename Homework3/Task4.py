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

def convert_to_binary(dec_number):
    bin_number = []
    while dec_number > 1:
        bin_number.append(dec_number % 2)
        dec_number = dec_number//2

    bin_number.append(dec_number)

    for _ in range(24-len(bin_number)):
        bin_number.append(0)
    
    bin_number = bin_number[::-1]

    return bin_number

num = int(enter_digit('Введите число: '))
flag_negative = 1
if num < 0:
    flag_negative = -1
    num *= flag_negative

result = convert_to_binary(num)

if flag_negative == -1:
    print(*binary_convert_to_negative(result), sep = '')
else:
    print(*result, sep = '')


