from functools import reduce
def create_tuples(values, ind):
    return list(zip(ind, values))


def filtr(array):
    for i in range(len(array)-1, -1, -1):
        num = []
        for c in array[i][1]:
            num.append(ord(c))
        if sum(num) % array[i][0] == 0:
            lang = array[i][1].upper()
            del array[i]
            array.insert(i, (reduce(lambda x,y: x + y, num), lang))
        else:
            del array[i]
    return array


lan = ['python', 'c#', 'kobol', 'pascal', 'c++', 'assembler',
       'r', 'java', 'go', 'fortran', 'scratch', 'php']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
my_tup = create_tuples(lan, num)
print(my_tup)
res = filtr(my_tup)
print(res)

def filter_list(tuples_list): 
    filtered = filter(lambda lang_list: reduce(lambda a,b: a+b, [ord(char) for char in lang_list[1]]) % lang_list[0]==0, tuples_list)
    result_list = list(map(lambda elem: (reduce(lambda a,b: a+b, [ord(char) for char in elem[1]]), elem[1]), filtered)) 
    result = sum([num for num, _ in result_list]) 
    return result_list, result