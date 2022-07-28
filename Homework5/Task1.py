def pattern_delete(text,sample):
    return ' '.join(filter(lambda word: sample not in word, text))

s = [w.lower() for w in input('Введите тект : ').split()]
sample  = input('Введите шаблон для удаления :').lower()
print(pattern_delete(s, sample))
