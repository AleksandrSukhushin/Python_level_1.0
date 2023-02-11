# Модуль функции /start
import game
from loader import dp
from aiogram.types import Message

@dp.message_handler(commands = ['start'])
async def mes_start(message: Message):
    name = message.from_user.first_name
    for duel in game.total:
        if name == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        await message.answer(f'Приветствую, {name}!\n'
                              '\nХочешь сыграть в КОНФЕТЫ?\n'
                              'Условия максимальны простые:\n'
                              '1. Два игрока берут со стола конфеты по очереди, но не более 28 за один раз и не менее 1;\n'
                              '2. Первый ход определяется рандомным жребием;\n'
                              '3. Победу одерживает игрок, забравший со стола последние конфеты!\n'
                             f'{name}, чтобы начать игру нажми любую кнопку!\n'
                              'Желаю успехов!')
    my_game = [message.from_user.id, name, 150]
    game.total.append(my_game)
