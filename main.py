from aiogram import Bot, Dispatcher
import asyncio
from handlers.commands import router as router_cmd
from handlers.hendler_text import router as router_txt
from handlers.callback import router as router_clb
from config import TOKEN
from global_data import global_context
from db.database import DataBase
from middlewares.i18n import I18nMiddleware
from middlewares.account import AccountMiddlewares

async def start_up():
    global_context.set(DataBase())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(router_cmd, router_txt, router_clb)
    dp.startup.register(start_up)
    dp.update.middleware(I18nMiddleware())
    dp.update.middleware(AccountMiddlewares())

    asyncio.run(main())
