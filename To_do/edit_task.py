import json as j
import my_library as ml
import new_task_enter as nt
path  = r'D:\По работе\ГИКБРЕЙНС\2 модуль\Знакомство с Python\Seminar\To_do\tasks_list.json'
    
def edit_task(task_list):
    while True:
        id = int(ml.enter_digit('Введите Id задачи: '))-1
        if id not in range(len(task_list)):
            print('Некорректный Id! Повторите ввод.')
        else:
            break
    print(""" 
            1 - Редактирование задачи
            2 - Удаление задачи""")
    while True:
        choice = input('    Ваш выбор -> ')
        if choice in ('1','2'):
            break
        else:
            print('     Некорректный ввод, Попробуйте еще раз')
    if choice == '2':
        del task_list[id]
        print('Задача удалена!')
        with open(path, 'w', encoding='UTF-8') as file:
            j.dump(task_list, file, indent = 2, ensure_ascii=False)
        return
    else:
        task = task_list[id]
        for k in task:
            if k == 'Приоритет':
               task[k] = nt.priority()
               continue
            if k == 'Статус':
               task[k] = nt.status_choice()
               continue
            task[k] = input(k + ': ')
        with open(path, 'w', encoding='UTF-8') as file:
            j.dump(task_list, file, indent = 2, ensure_ascii=False)
        return
