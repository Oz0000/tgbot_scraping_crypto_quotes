from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import CommandStart
from config import price

token = '6682955283:AAFawNwUZ5lteDio3ASaagAZpBcxZ-ynjYA'
dp = Dispatcher()
currency = 'usd'
of_what = ''

@dp.message(CommandStart())
async def start(message):
    await message.answer('hey kid. This is Bot of Quotes')
    await message.answer('Example message: btc usd.\nDefault currency is usd, you can not write it and the value will be displayed in usd.', parse_mode='HTML')


@dp.message()
async def answer1(message):
    st = message.text.split()
    global of_what, currency
    of_what = st[0]
    if len(st) > 1:
        currency = st[1]
    await message.answer(price(of_what, currency))


async def main():
    tb = Bot(token=token)
    await dp.start_polling(tb)


if __name__ == '__main__':
    asyncio.run(main())
