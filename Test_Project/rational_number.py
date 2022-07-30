# Readme: 
# Модуль принимает на вход строку. Возвращает число типа float. Строка должна представлять собой арифметическое выражение 
# и может быть любой длинны. Калькулятор работает с отрицательными и вещественными числами. Выполняет функции сложения, 
# вычитания, деления, умножения, возведения в степень и вычисляет остаток от деления. Порядок действий калькулятор не распознает.
# Необходимо определять его путем заключения приоритетных операций в скобки. 
# Если выражение содержит операции в скобках, во избежании ошибок калькулятор проверит соответствие открывающих скобок закрывающим. 
# Если соотношение скобок некорректно. Программа вернет сообщение об ошибке. Также программа уберет из исходной строки пробелы.
# Прочие проверки (на буквы и символы) не реализованы. Оставляю коллегам.
# 

def div(a,b):
    return a/b
def mult(a,b):
    return a*b
def plus(a,b):
    return a+b
def minus(a,b):
    return a - b
def row(a,b):
    return a**b
def rest(a,b):
    return a%b

def neg_check(s, oper):
    neg_flag = []
    if s.startswith('-'):
        s = s[1:]
        neg_flag.append(-1)
    else:
        neg_flag.append(1)
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '-' and s[i-1] in oper:
            neg_flag.append(-1)
            s = s[:i]+s[i+1:]
            n-=1
        elif s[i].isdigit() and s[i-1] in oper and s[i-2].isdigit():
            neg_flag.append(1)
        i+=1
    return s, neg_flag

def do_calc(s):
    oper = {'/': div, '*': mult, '+': plus, '-': minus,'^': row, '%': rest}
    s, neg_flag = neg_check(s, oper.keys())
    #print(s)
    #print(neg_flag)
    act = []
    for c in s:
        if c in oper.keys():
            s = s.replace(c, ' ', 1)
            act.append(c)
    n = (list(map(lambda n, f: n*f,list(map(float, s.split())), neg_flag)))
    #print(n)
    #print(act)
    res = oper[act[0]](n[0], n[1])
    for i in range(1, len(act)):
        res = oper[act[i]](res,n[i+1])
    return res

def bracket_check(s):           # Проверка на соответствие закрывающих скобок открывающим
    return sum(map(lambda br: 1 if br =='(' else -1, [elem for elem in s if elem == '(' or elem == ')']))

def reduce_brackets(s):         #Закрывает скобки
    while '(' in s:
        end = s[s.find(')')+1:]
        a = s[:s.find(')')]
        bracket = a[a.rfind('(')+1:]
        start = a[:a.rfind('(')]
        s = start + str(do_calc(bracket)) + end
    return s

def start_modul(input_s:str):
    input_s = input_s.replace(' ','')
    braсkets_status = bracket_check(input_s)
    if braсkets_status != 0:
        return 'ОШИБКА в последовательности скобок'
    if input_s.find('(') !=-1:
        input_s = reduce_brackets(input_s)
    return do_calc(input_s)    

#print(start_modul(input('Введите выражение: ')))
print(start_modul('156/(63-15)+((23-15)^2)+(135-51)*3/4/5*26'))