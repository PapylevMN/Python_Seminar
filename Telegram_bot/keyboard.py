from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup 
from aiogram.utils.callback_data import CallbackData

task_cb = CallbackData('task', 'id', 'action')

cancel_kb = ReplyKeyboardMarkup([['/Отмена']], resize_keyboard=True, one_time_keyboard=True)

kb_go = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/Меню')
b2 = KeyboardButton('/Справка')
kb_go.add(b1).insert(b2)

def ikb():
    ikb = InlineKeyboardMarkup(row_width = 5)
    b1 = InlineKeyboardButton('Ввод новой задачи', callback_data= 'new_task')
    b2 = InlineKeyboardButton('Игра Конфетки', callback_data='candy')
    b3 = InlineKeyboardButton('Вывести все', callback_data='print_all')
    ikb.add(b1).add(b2).add(b3)
    return ikb

def task_ikb(task_id: int):
    task_ikb = InlineKeyboardMarkup(row_width = 2)
    t_btn1 = InlineKeyboardButton('Удалить', callback_data= task_cb.new(task_id, 'delete'))
    t_btn2 = InlineKeyboardButton('Редактировать', callback_data=task_cb.new(task_id, 'edit'))
    task_ikb.add(t_btn1).insert(t_btn2)
    return task_ikb

def priority_ikb():
    prior_ikb = InlineKeyboardMarkup(row_width = 5)
    b1 = InlineKeyboardButton('Срочно', callback_data= 'Срочно')
    b2 = InlineKeyboardButton('Без срока', callback_data='Без срока')
    prior_ikb.add(b1).insert(b2)
    return prior_ikb

def status_ikb():
    stat_ikb = InlineKeyboardMarkup(row_width = 5)
    b1 = InlineKeyboardButton('Выполнено', callback_data= 'Выполнено')
    b2 = InlineKeyboardButton('Не выполнено', callback_data='Не выполнено')
    stat_ikb.add(b1).insert(b2)
    return stat_ikb
