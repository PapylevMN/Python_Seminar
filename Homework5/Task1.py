s = [w.lower() for w in input('Введите тект : ').split()]
sample  = input('Введите шаблон для удаления :').lower()
for i in range(len(s)-1, -1, -1):
    if s[i].find(sample) != -1:
        del s[i]
print(' '.join(s))