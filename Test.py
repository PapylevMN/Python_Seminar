
a = ['1','2', '3', 'a']
s = 'asdada'
r = any(list(map(lambda elem: elem in s,a)))
print(r)

