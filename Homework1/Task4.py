q = ('1', '2', '3', '4')
quorter = input('Введите номер четверти:')
if quorter not in q:
    print('Некорректный ввод!')
elif quorter == '1':
    print('Х > 0, Y > 0')
elif quorter == '2':
    print('Х < 0, Y > 0')
elif quorter == '3':
    print('Х < 0, Y > 0')
elif quorter == '4':
    print('Х > 0, Y < 0')
