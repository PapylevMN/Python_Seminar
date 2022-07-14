n = int(input())
dic = {}
for _ in range(n):
    key, value = input().split(': ')
    dic[key] = value
m = int(input())
for _ in range(m):
    name = input().capitalize()
    if name in dic.keys():
        print(dic[name])
    else:
        print('Не найдено')
