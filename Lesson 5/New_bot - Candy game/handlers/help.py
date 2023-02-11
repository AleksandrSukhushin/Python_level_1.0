# Модуль функции /help
from loader import dp
from aiogram.types import Message

@dp.message_handler(commands = ['help'])
async def mes_help(message: Message):
    name = message.from_user.first_name
    await message.answer('Sorry, помочь тебе нечем\n'
                        f'\n{name}, желаю тебе удачной игры!')
    print(name)
