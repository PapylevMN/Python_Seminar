import json as j
import csv
path_j  = r'D:\По работе\ГИКБРЕЙНС\2 модуль\Знакомство с Python\Seminar\To_do\tasks_list.json'
path_c  = r'D:\По работе\ГИКБРЕЙНС\2 модуль\Знакомство с Python\Seminar\To_do\tasks_list.csv'
    
def to_csv():
    try:
        with open (path_j, 'r', encoding='UTF-8') as file:
            data = j.load(file)
            headers = data[0].keys()

            with open(path_c, 'w', encoding='UTF-8') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerow(headers)
                for elem in data:
                    rec = (val for val in elem.values())
                    writer.writerow(rec)
        print('Список задач переведен в формат CSV')
        return
    except:
        print('Оригинальный JSON файл не найден!')
        return