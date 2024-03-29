# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def second_coming(lst, elem): 
    return [i for i, element in enumerate(lst) if elem in element][1] if len(lst) > 2 else 0

def check_second(data):
    count = 0
    for i in range(len(data[0])):
        if data[0][i] == data[1] and count == 1:
            return i
        if data[0][i] == data[1]:
            count += 1
    return -1
array = [["qwe", "asd", "zxc", "qwe", "ertqwe"], ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ["йцу", "фыв", "ячс", "цук", "йцукен"], ["123", "234", 123, "567"], []]
sample = ['qwe', 'йцу', 'йцу', '123', '123']
res = list(map(check_second, zip(array,sample)))
for i in range(len(array)):
    print(f' Список: {array[i]}, ищем: {sample[i]}, ответ {res[i]}')