import my_library as ml
import random
def player_move(name, num, bot):
    if bot:
        if num <= 28:
            q = num
        else:
            q = num%29 if num%29 != 0 else random.randint(1,28)
        num -=q
        print(f'{name} взял {q} конфет')
    else:
        pl1 = ml.enter_candy(f'{name}, cколько конфет возьмете? :')
        num -= pl1
    return num

def game(quont, bot):
    name1 = input('Введите имя игрока 1: ')
    name2 = input('Введите имя игрока 2: ') if not bot else 'Робот Вертер'
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
        quont = player_move(name1, quont, False) if flag else player_move(name2, quont, bot)
        print(f'Осталось {quont}') if quont > 0 else print('Осталось 0')
    print(f'{name1} ВЫИГРАЛ!') if flag else print(f'{name2} ВЫИГРАЛ!')            
    return

n = 121
run = True
print('==============================НАЧИНАЕМ ИГРУ "ГОНКА К ДИАБЕТУ"=====================================')
print(f'На столе {n} конфет, берите по очереди не более 28 шт. Кто делает последний ход, тот забирает все!')
while run:
    print('- 1 - Игра с компьютером')
    print('- 2 - 2 Игрока')
    mode = input('Выберите режим игры (1 или 2): ')
    bot = True if mode == '1' else False
    game(n, bot)
    end = input('Хотите сыграть еще? Y/N? ')
    run = True if end.lower() == 'y' or end.lower() == 'д' else False
