# 1- Определить, присутствует ли в заданном списке строк, некоторое число

s = 'Мама сшила м0не штаны и7з бере9зовой кор45ы 893.'
res = ' '.join(list(filter(lambda word: all(map(lambda c: c.isalpha(), word)), s.split())))
print(res)