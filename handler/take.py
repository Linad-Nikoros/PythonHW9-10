import random
from loader import dp
from aiogram.types import Message
import game
from game import total_candies, set_total


@dp.message_handler()
async def mes_help(message: Message):
    global total_candies
    if set_total[message.from_user.id] == True:  
        try:
            int(message.text)
            total_candies[message.from_user.id] = int(message.text)
        except:
            await message.answer("Введите целое число")
        
        await message.answer(f"Вы положили на стол {message.text}. Сколько конфет хотите взять?")
        set_total[message.from_user.id] = False

    elif message.from_user.id in total_candies:
        count = message.text
        if count.isdigit() and 0 < int(count) < 29:
            total_candies[message.from_user.id] -= int(count)
            if await check_win(message, message.from_user.first_name):
                return True
            
            await message.answer(f'{message.from_user.first_name} взял {count} конфет и на столе осталось {total_candies[message.from_user.id]}\n'
                                 f'Теперь ход бота...')
            bot_take = random.randint(1, 28) if total_candies[message.from_user.id] > 28 else total_candies[message.from_user.id]
            total_candies[message.from_user.id] -= bot_take
            if await check_win(message, 'Бот'):
                return True
            
            await message.answer(f'Бот  взял {bot_take} конфет и '
                                 f'на столе осталось {total_candies[message.from_user.id]}\n'
                                 f'Теперь твой ход...')
        else:
            await message.answer(f'Введите число от 1 до 28')


async def check_win(message: Message, win: str):
    if total_candies[message.from_user.id] <= 0:
        await message.answer(f'{win} победил! ')
        total_candies.pop(message.from_user.id)
        set_total[message.from_user.id] = False
        return True
    return False