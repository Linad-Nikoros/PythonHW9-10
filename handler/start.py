import game
from loader import dp
from aiogram.types import Message
from game import set_total,total_candies

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for id in game.total_candies:
        if message.from_user.id == id :
            await message.answer('Ты уже начал игру! Играй давай!'
                                 'Введите количество конфет,которое будет лежать на столе.')
            break
    else:
        await message.answer(f'Привет, {message.from_user.full_name}'
                             f' Мы будем играть в конфеты. Бери от 1 до 28...'
                            'Введите количество конфет,которое будет лежать на столе.')
    total_candies[message.from_user.id] = 0  
    set_total[message.from_user.id] = True