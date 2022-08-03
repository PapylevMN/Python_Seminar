import json as j
import edit_task as edit

def print_head():
    print("""
_________________________________________________________________________________________________________________________
 Id |        Дата           |        Срок          |        Задача        |       Приоритет     |         Статус        | 
-------------------------------------------------------------------------------------------------------------------------""")
    return

def print_all():
    path  = r'D:\По работе\ГИКБРЕЙНС\2 модуль\Знакомство с Python\Seminar\To_do\tasks_list.json'
    with open (path, 'r', encoding='UTF-8') as file:
        to_do_list  = j.load(file)
    print_head()
    for task in to_do_list:
        for k in task.keys():
            print(f"  {task[k].ljust(18, ' ')}   ", end = '|')
        print()
    return


def search():
    while True:
        search_str = input('Введите строку для поиска: ').lower()
        path  = r'D:\По работе\ГИКБРЕЙНС\2 модуль\Знакомство с Python\Seminar\To_do\tasks_list.json'
        with open (path, 'r', encoding='UTF-8') as file:
            to_do_list  = j.load(file)
        find_flag = any(list(map(lambda elem: any(list(map(lambda val: search_str in val, [s.lower() for s in elem.values()]))), to_do_list)))
        if not find_flag:
            if input('Задачи с такими параметрами поиска не найдено! Повторить поиск? (Д/Н)') in ('Y','y','Д','д'):
                continue
            else:
                return
        break
    print_head()
    for i in range(len(to_do_list)):
        if any(list(map(lambda val: search_str in val, [s.lower() for s in to_do_list[i].values()]))):
            print(f'  {i+1}  ', end = '|')
            for k in to_do_list[i].keys():
                print(f"  {to_do_list[i][k].ljust(18, ' ')}   ", end = '|')
            print()
    if input('Желаете продолжить работу с задачами? (Д/Н)') not in ('Y','y','Д','д'):
        return
    else:
        edit.edit_task(to_do_list)
    return
