# Модуль обработчика пользовательского интерфейса
import random
from aiogram import types
from loader import dp
import time

# Инициализация переменных
max_count = 150
new_game = False
total = 0
lot = 0
current = 0

# Функция приветствия игрока (старт бота)
@dp.message_handler(commands = ['start'])
async def mes_start_bot(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Приветствую, {name}!\n'
                          '\nХочешь сыграть в КОНФЕТЫ?\n'
                          'Условия максимальны простые:\n'
                          '1. Два игрока берут со стола конфеты по очереди, но не более 28 за один раз и не менее 1;\n'
                          '2. Первый ход определяется рандомным жребием;\n'
                          '3. Победу одерживает игрок, забравший со стола последние конфеты!')
    time.sleep(1)
    await message.answer('Жми -> /help, чтобы изучить основные команды.')

# Функция памятки основных команд для игрока
@dp.message_handler(commands = ['help'])
async def mes_help_user(message: types.Message):
    name = message.from_user.first_name
    await message.answer('Памятка:\n'
                        '/start - для запуска бота;\n'
                        '/set [ваше число] - задать количество конфет для игры;\n'
                        '/game - начать игру против бота;\n'
                        f'\n{name}, желаю тебе удачной игры!')

# Функция начала игры
@dp.message_handler(commands = ['game'])
async def mes_game(message: types.Message):
    global new_game
    global total
    global max_count
    global lot
    new_game = True
    total = max_count
    lot = random.randint(0, 1)
    name = message.from_user.first_name
    if lot:
        await message.answer(f'Игра началась!\n'
                             f'Первый ход за тобой, {name} ...')
    else:
        await message.answer(f'Игра началась!\nПервым ходит Бот ...')
        await mes_bot(message)

# Функция игрового бота
async def mes_bot(message: types.Message):
    global total
    global new_game
    bot_take = 0
    name = message.from_user.first_name
    if 0 < total < 29:
        bot_take = total
        total -= bot_take
        await message.answer(f'Бот забирает последние -> {bot_take} конфет\n'
                             'Бот одержал победу!')
        await message.answer(f'{name}, желаешь отыграться? Жми -> /game')
        new_game = False
    else:
        remainder = total % 29
        bot_take = random.randint(1, 29)
        # bot_take = remainder if remainder != 0 else 28 - не понравилось, что Бот постоянно побеждает))
        total -= bot_take
        await message.answer(f'Бот взял -> {bot_take} конфет\n'
                             f'На столе осталось -> {total}\n')
        await message.answer(f'Твой ход, {name} ...')

# Функция изменения параметров (задание нового количества конфет)
@dp.message_handler(commands = ['set'])
async def mes_set(message: types.Message):
    global max_count
    global new_game
    count = message.text.split()[1]
    name = message.from_user.first_name
    if not new_game:
        if count.isdigit():
            max_count = int(count)
            await message.answer(f'Конфет теперь будет -> {max_count}')
        else:
            await message.answer(f'{name}, напишите цифрами!')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры!!!')

# Функция, описывающая процесс игры (конфеты берутся по очереди)
@dp.message_handler()
async def mes_take(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global lot
    name = message.from_user.first_name
    count = message.text
    if new_game:
        if message.text.isdigit() and 0 < int(count) < 29:
            total -= int(count)
            if total <= 0:
                await message.answer(f'Ура! {name}, ты победил!')
                await message.answer('Желаешь подтвердить успех? Жми -> /game')
                new_game = False
            else:
                await message.answer(f'{name} взял -> {count} конфет\n'
                                     f'На столе осталось -> {total}')
                await mes_bot(message)
        else:
            await message.answer(f'{name}, надо указать ЧИСЛО от 1 до 28!')
