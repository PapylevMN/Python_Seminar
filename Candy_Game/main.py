
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
from random import randint

def start(update, context):
    global QUONT
    QUONT = 140
    context.bot.send_message(update.effective_chat.id, 
        'Это Бот, Сыграем в конфетки\nНа столе 140 конфет, берем по очереди не более 28 шт. Кто делает последний ход, тот забирает все!\nДавайте кинем жребий кто будет ходить первым!'
        )
    turn = randint(0,1)
    if turn == 0:
        context.bot.send_message(update.effective_chat.id, 'Первый ход мой!')
        return game(update, context)
    else:
        context.bot.send_message(update.effective_chat.id, f'Первый ход Выш, берите конфеты!')
        return MOVE

def game(update, context):
    global QUONT
    if QUONT <= 28:
        take = QUONT 
    else:
        take = QUONT % 29 if QUONT % 29 != 0 else randint(1,28)
    QUONT -= take
    if QUONT > 0:
        context.bot.send_message(update.effective_chat.id, f'Я взял {take} конфет.')
        context.bot.send_message(update.effective_chat.id, f'Осталось {QUONT} конфет, Теперь Ваша очередь!')
        return MOVE
    else:
        context.bot.send_message(update.effective_chat.id, f'Я взял {take} конфет.')
        context.bot.send_message(update.effective_chat.id, 'Осталось 0 конфет. Я ВЫИГРАЛ!')
        cancel(update, context)
        #return ConversationHandler.END
 
def move(update, context):
    global QUONT
    take = update.message.text
    if not take.isdigit() or int(take) > 28:
        update.message.reply_text('Введите число не более 28!')
        return MOVE
    QUONT -= int(take)
    if QUONT > 0:
        context.bot.send_message(update.effective_chat.id, f'Осталось {QUONT} конфет.')
        game(update, context)
    else:
        context.bot.send_message(update.effective_chat.id, 'Осталось 0 конфет. ВЫ ВЫИГРАЛИ!')
        cancel(update, context)
        #return ConversationHandler.END
    
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Игра окончена')
    return ConversationHandler.END

if __name__ == '__main__':
    QUONT = 140
    MOVE = 1
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            #EXIT_GAME: [MessageHandler(Filters.text, cancel)],
            MOVE: [MessageHandler(Filters.text, move)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    print('server start')
    updater.idle()
    