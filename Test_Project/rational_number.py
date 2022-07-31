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

def do_calc(expression, operation):
    #oper = {'/': div, '*': mult, '+': plus, '-': minus,'^': row, '%': rest}
    expression, neg_flag = neg_check(expression, operation.keys())
    act = []
    for c in expression:
        if c in operation.keys():
            expression = expression.replace(c, ' ', 1)
            act.append(c)
    n = (list(map(lambda n, f: n*f,list(map(float, expression.split())), neg_flag)))
    res = operation[act[0]](n[0], n[1])
    for i in range(1, len(act)):
        res = operation[act[i]](res,n[i+1])
    return res

def bracket_check(s):           # Проверка на соответствие закрывающих скобок открывающим
    return sum(map(lambda br: 1 if br =='(' else -1, [elem for elem in s if elem == '(' or elem == ')']))

def reduce_brackets(expression, operation):         #Закрывает скобки
    while '(' in expression:
        end = expression[expression.find(')')+1:]
        temp = expression[:expression.find(')')]
        bracket = temp[temp.rfind('(')+1:]
        start = temp[:temp.rfind('(')]
        expression = start + str(do_calc(bracket, operation)) + end
    return expression

def start_modul(input_s:str):
    operation_list = {'/': div, '*': mult, '+': plus, '-': minus,'^': row, '%': rest}
    input_s = input_s.replace(' ','')
    braсkets_status = bracket_check(input_s)
    if braсkets_status != 0:
        return 'ОШИБКА в последовательности скобок'
    if input_s.find('(') !=-1:
        input_s = reduce_brackets(input_s, operation_list)
    if any(list(map(lambda elem: elem in input_s, operation_list.keys()))):
        return do_calc(input_s, operation_list)
    else:
        return input_s


print(start_modul('((63-15)+(23-15))'))
#print(start_modul(input('Введите выражение: ')))
#print(start_modul('156/(63-15)+((23-15)^2)+(135-51)*3/4/5*26'))
#print(start_modul('((63-15)+((23-15))'))