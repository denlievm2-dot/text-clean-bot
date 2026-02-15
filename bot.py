
import asyncio
import os
import re
import emoji
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = os.getenv("TOKEN")

PREFIX_TEXT = "аккаунт зарегистрирован на 15 летнюю девочку,которая опять же пойдет в полицию со мной,ну можем мирно решить,выбор только за тобой,двоих уже так закрыли,также переписка будет отправлена родственникам и знакомым. Выбор за тобой как разойтись,мирно или по плохому.\n\n"

bot = Bot(token=TOKEN)
dp = Dispatcher()


def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')


def remove_interest_line(text):
    pattern = r"👁?\s*Интересовались этим:.*"
    return re.sub(pattern, "", text)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Отправь текст для обработки.")


@dp.message()
async def clean(message: Message):
    if message.text:
        text = message.text
        text = remove_emoji(text)
        text = remove_interest_line(text)
        text = text.strip()
        await message.answer(PREFIX_TEXT + text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
