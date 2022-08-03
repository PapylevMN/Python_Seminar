# import json as j
# path  = r'D:\По работе\ГИКБРЕЙНС\2 модуль\Знакомство с Python\Seminar\To_do\tasks_list.json'

# def status_choice():
#     st = ('Не сделано', 'В работе', 'Сделано')
#     print("""Статус:    Выберите варриант:
#                         1 - Не сделано
#                         2 - В работе
#                         3 - Сделано """)
#     while True:
#         choice = int(input('    Ваш выбор -> '))
#         if choice in (1,2,3):
#             return st[choice-1]
#         else:
#             print('     Некорректный ввод, Попробуйте еще раз')

# def priority():
#     prior = ('Срочно', 'Терпит', 'Без срока')
#     print("""Приоритет: Выберите вариант:
#                         1 - Срочно
#                         2 - Терпит
#                         3 - Без срока """)
#     while True:
#         choice = int(input('    Ваш выбор -> '))
#         if choice in (1,2,3):
#             return prior[choice-1]
#         else:
#             print('     Некорректный ввод, Попробуйте еще раз')

# def enter_task():
#     run = True
#     result = []
#     keys = ['Дата', 'Срок', 'Задача', 'Приоритет', 'Статус']
#     print('Ввод новой задачи:')
#     while run:
#         keys = ['Дата', 'Срок', 'Задача', 'Приоритет', 'Статус']
#         values = ['' for n in keys]
#         for i in range(len(keys)):
#             if keys[i] == 'Приоритет':
#                 values[i] = priority()
#             if keys[i] == 'Статус':
#                 values[i] = status_choice()
#         values[i] = input(keys[i] + ': ')
#         task = dict(zip(keys,values))
#         result.append(task)
#         next_task = input('Ввести еще задачу? (Д/Н) ')
#         if input('Ввести еще задачу? (Д/Н) ') == 'Д':
#             continue
#         else:
#             break
#     print(result)
#     return result 