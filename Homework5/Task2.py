import my_library as ml
import random
def player_move(name, num):
    pl1 = int(ml.enter_candy(f'{name}, cколько конфет возьмете? :'))
    num -= pl1
    return num

def bot_move(num):
    q = random.randint(1,28)
    num -=q
    print(f'Бот взял {q} конфет')
    return num

def one_player(quont):
    name1 = input('Введите имя игрока :')
    turn  = random.randint(0,1)
    if turn == 0:
        print(f'Первый ход {name1}: ')
        flag = True
    else:
        print('Первый ход Бота:')
        flag = False
    flag = not flag
    while quont > 0:
        flag = not flag
        quont = player_move(name1, quont) if flag else bot_move(quont)
        print(f'Rest is {quont}')
    print(f'{name1} ВЫИГРАЛ!') if flag else print('Бот ВЫИГРАЛ!')            
    return

def two_player(quont):
    name1 = input('Введите имя игрока 1: ')
    name2 = input('Введите имя игрока 2: ')
    turn  = random.randint(0,1)
    if turn == 0:
        print(f'Первый ход {name1}:')
        flag = True
    else:
        print(f'Первый ход {name2}:')
        flag = False
    flag = not flag
    while quont > 0:
        flag = not flag
        quont = player_move(name1, quont) if flag else player_move(name2, quont)
        print(f'Rest is {quont}')
    print(f'{name1} ВЫИГРАЛ!') if flag else print('Игрок 2 ВЫИГРАЛ!')            
    return

n = 121
run = True
while run:
    print('==============================НАЧИНАЕМ ИГРУ "ГОНКА К ДИАБЕТУ"=====================================')
    print(f'На столе {n} конфет, берите по очереди не более 28 шт. Кто делает последний ход, тот забирает все!')
    print('- 1 - Игра с компьютером')
    print(' -2 - 2 Игрока')
    mode = input('Выберите режим игры (1 или 2): ')
    one_player(n) if mode == '1' else two_player(n)
    end = input('Хотите сыграть еще? Y/N? ')
    run = True if end.lower() == 'y' else False

