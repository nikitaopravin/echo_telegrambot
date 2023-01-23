import os
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(filename="log.txt", level=logging.INFO)

TOKEN=os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello, {user_name}!'
    logging.info(f'{user_name} {user_id} send message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def transliteration(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    translit_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 
        'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y',
        'Ъ': 'IE', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': ''}
    text = message.text.upper()
    for chr in translit_dict.keys():
        text = text.replace(chr, translit_dict[chr])
    logging.info(f'{user_name} {user_id} send message: {message.text}')
    await bot.send_message(user_id, text)
       
if __name__ == '__main__':
    executor.start_polling(dp)
