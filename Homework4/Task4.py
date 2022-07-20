with open('data.txt', encoding='utf-8') as file:
    data = list(map(str.strip, file.readlines()))

for l in range(len(data)):
    newline = data[l].split()
    for i in range(len(newline)-1, -1, -1):
        for c in newline[i]:
            if c.isdigit():
                del newline[i]
                break
    data[l] = ' '.join(newline)
        
with open('data.txt', 'w', encoding='utf-8') as file:
    for line in data:
        print(line, file = file)

print('Исходный файл перезаписан!')