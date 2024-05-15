from aiogram.fsm.context import FSMContext
from aiogram.types.dice import DiceEmoji
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.markdown import hbold

from .routers import film_router
from .routers.film import edit_or_answer, show_films_command

# Завантажимо дані середовища з файлу .env(За замовчуванням)
load_dotenv()

# Усі обробники варто закріплювати за Router або Dispatcher
root_router = Router()
root_router.include_routers(film_router)


# Обробник для команди /start
@root_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Вітаю, {hbold(message.from_user.full_name)}!\n Команди:\n films - список фільмів \n "
                         f"filmcreate - додати фільм")


@root_router.message(Command("dice"))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)



# Головна функція пакету
async def main() -> None:
    # Дістанемо токен бота з середовища
    TOKEN = getenv("BOT_TOKEN")
    # Створимо об'єкт Bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(root_router)
    # Почнемо обробляти події для бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
