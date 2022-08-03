 
def priority(c, nums, act, operation):
    ind = act.index(c)
    temp_res = operation[c](nums[ind], nums[ind + 1])
    del nums[ind+1]
    del nums[ind]
    nums.insert(ind, temp_res)
    del act[ind]
    return nums, act

def check_for_negative_number(s, oper):
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
    expression, neg_flag = check_for_negative_number(expression, operation.keys())
    act = []
    for c in expression:
        if c in operation.keys():
            expression = expression.replace(c, ' ', 1)
            act.append(c)
    numbers = (list(map(lambda n, f: n*f,list(map(float, expression.split())), neg_flag)))
    priority_operation = '^*/'
    if any(list(map(lambda elem: elem in priority_operation, act))):
        for _ in range (act.count('*') + act.count('^') + act.count('/')):
            if '^' in act:
                numbers, act = priority('^', numbers, act, operation)
                continue
            if '*' in act and '/' in act:
                if act.index('*') < act.index('/'):
                    numbers, act = priority('*', numbers, act, operation)
                    continue
                else:
                    numbers, act = priority('/', numbers, act, operation)
                    continue
            if '/' in act:
                numbers, act = priority('/', numbers, act, operation)
                continue                
            if '*' in act:
                numbers, act = priority('*', numbers, act, operation)
    if len(act) == 0:
        return numbers[0]
    else:
        res = operation[act[0]](numbers[0], numbers[1])
        for i in range(1, len(act)):
            res = operation[act[i]](res, numbers[i+1])
        return res

def bracket_check(s):                               # Проверка на соответствие закрывающих скобок открывающим
    return sum(map(lambda br: 1 if br =='(' else -1, [elem for elem in s if elem == '(' or elem == ')']))

def reduce_brackets(expression, operation):         # Ищет выражение в скобках и вычисляет его
    while '(' in expression:
        end = expression[expression.find(')')+1:]
        temp = expression[:expression.find(')')]
        bracket = temp[temp.rfind('(')+1:]
        start = temp[:temp.rfind('(')]
        expression = start + str(do_calc(bracket, operation)) + end
    return expression

def start_modul(input_s:str):
    operation_list = {'/': lambda a,b:a/b, '*': lambda a,b: a*b, '+': lambda a,b: a+b, '-': lambda a,b: a-b,'^': lambda a,b: a**b, '%': lambda a,b: a%b}
    input_s = input_s.replace(' ','')
    braсkets_status = bracket_check(input_s)
    if braсkets_status != 0:
        return 'ОШИБКА в последовательности скобок'
    if input_s.find('(') !=-1:
        input_s = reduce_brackets(input_s, operation_list)
    return do_calc(input_s, operation_list) if any(list(map(lambda elem: elem in input_s, operation_list.keys()))) else input_s

