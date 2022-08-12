



@dp.callback_query_handler(text = 'candy')
async def candy_game(callback: types.CallbackQuery, state: FSMContext):
    bank = 140
    await callback.message.answer(f'Давайте поиграем! На столе {bank} конфет. Возьмите не более 28 шт.', reply_markup=cancel_kb)
    await TaskStatesGroup.candy.set()
    await callback.answer()

    bot_move = True
    bank -= TAKEN_CANDY 
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