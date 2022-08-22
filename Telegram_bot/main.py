from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from config import TOKEN, ID
from keyboard import *
import database 
import random

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class TaskStatesGroup(StatesGroup):
    task_name = State()
    date = State()
    term = State()
    priority = State()
    status = State()
    new_task_name = State()
    candy = State()

HELP = """
<b>/Справка</b>    - список команд
<b>/Отмена</b>    - отмена операции
<b>/Меню</b>      - вывод меню
"""

async def on_startup(_):
    await database.database_connect()
    print('База данных подключена!')
    await bot.send_message(chat_id=ID, 
        text='<b>Добро пожаловать в планировщик дел!</b>', 
        parse_mode='HTML',
        reply_markup = kb_go)
    
    
    
async def show_all_tasks(callback: types.callback_query, tasks:list):
    for task in tasks:
        await bot.send_message(chat_id=ID, 
                                text = f'{task[0]}. <b>{task[3]}</b>\n Дата: {task[1]}\n Срок: {task[2]}\n Приоритет: {task[4]}\n Статус: {task[5]}', 
                                parse_mode='HTML',
                                reply_markup=task_ikb(task[0]))

@dp.message_handler(commands = ['Меню'])
async def start(message: types.Message):
    await bot.send_message(chat_id = ID, text = 'Выберите пункт меню:', reply_markup = ikb())
    await message.delete()

@dp.message_handler(commands = ['Справка'])
async def help(message: types.Message):
    await bot.send_message(chat_id = ID, text = HELP, parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands = ['Отмена'], state = '*')
async def cancel_task(message: types.Message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await message.answer('Отмена операции!', reply_markup=kb_go)
    await message.delete()

@dp.callback_query_handler(text = 'print_all')
async def show_all(callback: types.CallbackQuery):
    tasks = await database.get_all_tasks()
    if not tasks:
        await callback.message.delete()
        await callback.message.answer('Пока задач нет.')
        return await callback.answer()
    await callback.message.delete()
    await show_all_tasks(callback, tasks)
    await callback.message.answer('Это все задачи на сегодня!')

@dp.callback_query_handler(text = 'new_task')
async def add_task(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text='<b>Введите задачу:</b>', parse_mode='HTML' , reply_markup=cancel_kb)
    await TaskStatesGroup.task_name.set()

@dp.message_handler(state=TaskStatesGroup.task_name)
async def handle_task(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data['task_name'] = message.text
    await message.reply('Введите дату:')
    await TaskStatesGroup.next()

@dp.message_handler(state=TaskStatesGroup.date)
async def handle_date(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.reply('Введите срок:')
    await TaskStatesGroup.next()

@dp.message_handler(state=TaskStatesGroup.term)
async def handle_term(message: types.Message, state = FSMContext):
    async with state.proxy() as data:
        data['term'] = message.text
    await message.reply('Введите приоритет:', reply_markup=priority_ikb())
    await TaskStatesGroup.next()

@dp.callback_query_handler(state = TaskStatesGroup.priority, text = 'Срочно')
async def enter_prior(callback: types.CallbackQuery, state = FSMContext):
    async with state.proxy() as data:
        data['priority'] = callback.data
    await callback.message.answer('Выберите статус задачи:', reply_markup=status_ikb())
    await TaskStatesGroup.next()

@dp.callback_query_handler(state = TaskStatesGroup.priority, text = 'Без срока')
async def enter_prior(callback: types.CallbackQuery, state = FSMContext):
    async with state.proxy() as data:
        data['priority'] = callback.data
    await callback.message.answer('Выберите статус задачи:', reply_markup=status_ikb())
    await TaskStatesGroup.next()

@dp.callback_query_handler(state = TaskStatesGroup.status, text = 'Выполнено')
async def enter_prior(callback: types.CallbackQuery, state = FSMContext):
    async with state.proxy() as data:
        data['status'] = callback.data
    await database.add_new_task(state)
    await callback.message.answer('Запись добавлена!', reply_markup=kb_go)
    await state.finish()

@dp.callback_query_handler(state = TaskStatesGroup.status, text = 'Не выполнено')
async def enter_prior(callback: types.CallbackQuery, state = FSMContext):
    async with state.proxy() as data:
        data['status'] = callback.data
    await database.add_new_task(state)
    await callback.message.answer('Запись добавлена!', reply_markup=kb_go)
    await state.finish()

@dp.callback_query_handler(task_cb.filter(action = 'delete'))
async def delete_task(callback: types.CallbackQuery, callback_data: dict):
    await database.delete_task(callback_data['id'])
    await callback.message.reply('Задача удалена!')
    await callback.answer()

@dp.callback_query_handler(task_cb.filter(action = 'edit'))
async def edit_task(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.message.answer('Введите новое название задачи:', reply_markup=cancel_kb)
    await TaskStatesGroup.new_task_name.set()
    async with state.proxy() as data:
        data['task_id'] = callback_data['id']
    await callback.answer()

@dp.message_handler(state = TaskStatesGroup.new_task_name)
async def load_new_task_name(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        await database.edit_task(data['task_id'], message.text)
    await message.reply('Название задачи изменено!', reply_markup=kb_go)
    await state.finish()
    
@dp.callback_query_handler(text = 'candy')
async def candy_game(callback: types.CallbackQuery, state: FSMContext):
    bank = 140
    await callback.message.answer(f'Давайте поиграем! На столе {bank} конфет. Возьмите не более 28 шт.', reply_markup=cancel_kb)
    await TaskStatesGroup.candy.set()
    await callback.answer()

@dp.message_handler(state = TaskStatesGroup.candy)
async def take_candy(message:types.Message, state: FSMContext):
    # global TAKEN_CANDY
    # TAKEN_CANDY = int(message.text)
    bot_move = True
    bank -= intTAKEN_CANDY 
    await message.reply(f'Вы взяли {TAKEN_CANDY} конфет')
    bot_move = True
    bank -= TAKEN_CANDY 
    while bank > 0:
        if bot_move:
            bot_take = random.randint(1,28) if bank > 28  else bank
            bank -= bot_take
            bot_move = not bot_move
            await bot.send_message(chat_id=ID, text = f'Я беру {bot_take} конфет, остаток {bank} конфет!')    
        else:
            bank -= TAKEN_CANDY
            await bot.send_message(chat_id=ID, text = f'Вы взяли {TAKEN_CANDY} конфет, остаток {bank} конфет!')
            bot_move = not bot_move
    await bot.send_message(chat_id=ID, text = 'Я выиграл!') if bot_move else await bot.send_message(chat_id=ID, text = 'Вы выиграли!')
    await bot.send_message(chat_id=ID, text = 'Игра окончена!', reply_markup=kb_go)
    await state.finish()

if __name__ == '__main__':
    print('Bot is running')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    