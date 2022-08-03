import json as j

path  = r'D:\По работе\ГИКБРЕЙНС\2 модуль\Знакомство с Python\Seminar\Phone_book\phone_book.json'
with open (path, 'r', encoding='UTF-8') as file:
    phone_book  = j.load(file)

#phone_book = [{'id': {'Фамилия': 'Иванов', 'Имя': 'Семен', 'Отчество': 'Семенович', 'Телефон': {'моб.1': '+7 921 325-40-54', 'моб.2': '+7 935 654-54-87 ', 'раб.': '+7 818 056-87-45 ', 'дом.': ' '}, 'email': 'asdf@mail.ru'}}]
print(phone_book)
with open(path, 'w', encoding='UTF-8') as file:
    j.dump(phone_book, file, indent = 2, ensure_ascii=False)
            