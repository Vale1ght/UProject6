from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я - UProject6, но для тебя просто - Юпи.\n" 
                         "Я буду помогать тебе в скучнойстудентческой рутине. Чтобы узнать мои команды напиши \"/help\".")