res = []
res1 = []
bin = (0,1)
for x in bin:
    for y in bin:
        for z in bin:
            res.append(not (x or y or z))
            res1.append(not x and not y and not z)
print(*res)
print(*res1)
if res == res1:
    print('Исходное утверждение ИСТИННО!')
else:
    print('Исходное утверждение ЛОЖНО!')