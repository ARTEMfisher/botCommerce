import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.filters import Command
from static.api import TG_BOT_API_KEY

bot = Bot(token=TG_BOT_API_KEY)
dp = Dispatcher()

# Клавиатура с кнопкой "Начать"
startKb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Начать')]],
    resize_keyboard=True
)

# Основная клавиатура после нажатия "Начать"
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О проекте"),KeyboardButton(text="Комплектация+стоимость")],
        [KeyboardButton(text="Как приобрести"),KeyboardButton(text="Корзина")],
        [KeyboardButton(text="📞 Связаться с нами")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start (отправляет кнопку "Начать")
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Нажмите 'Начать', чтобы продолжить.", reply_markup=startKb)

# Обработчик кнопки "Начать" (показывает главное меню)
@dp.message(lambda message: message.text == "Начать")
async def start_button_handler(message: Message):
    await message.answer("Бот запущен! 🎉")
    await message.answer("Здравствуйте! Я автоматический бот КБ МиС. Вы можете узнать ответы на частые вопросы или связаться с техподдержкой.", reply_markup=keyboard)

async def main():
    print('start bot')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
