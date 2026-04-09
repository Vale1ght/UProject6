from aiogram import Router
from . import start

def get_handlers_router() -> Router:
    router = Router()

    # Подключение роутеров из файлов
    router.include_router(start.router)

    return router