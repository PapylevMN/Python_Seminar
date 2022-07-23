def rle_in():
    with open ('input.txt', encoding = 'utf-8') as file:
        data = list(map(str.strip, file.readlines()))
    res = []
    for line in data:
        s = ''
        count = 1
        c = line[0]
        for i in range(1,len(line)):
            new_c = line[i]
            if new_c == c:
                count+=1
            else:
                s += c if count == 1 else str(count) + c
                c = line[i]
                count = 1
        s += c if count == 1 else str(count) + c            
        res.append(s)
    with open('output.txt', 'w', encoding='utf-8') as file:
        for line in res:
            print(line, file = file)
    return res

def rle_out():
    with open ('output.txt') as file:
        data = list(map(str.strip, file.readlines()))
    res = []
    for line in data:
        s = ''
        n = ''
        for c in line:
            if c.isdigit():
                n += c
            else:
                s += c if n == '' else int(n)*c
                n = ''
        res.append(s)
    with open('input.txt', 'w', encoding='utf-8') as file:
        for line in res:
            print(line, file = file)
    return res
print('Сжатые данные :')
print(*rle_in(), sep = '\n')
print('Восстановленные данные :')
print(*rle_out(), sep = '\n')
