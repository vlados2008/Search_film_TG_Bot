from typing import Any, Awaitable, Callable
from aiogram.types import TelegramObject, User, Update
from aiogram import BaseMiddleware
from db.database import DataBase
from utils.i18n import i18n
from global_data import global_context

class AccountMiddlewares(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
    ) -> Any:

        if isinstance(event, Update):
            if event.message and event.message.text.startswith("/start"):
                return await handler(event, data)
        
        user_handler: User | None = data.get("event_from_user")

        if user_handler:
            db: DataBase = global_context.get()
            have_user_db = db.get_user(user_handler.id)
            if have_user_db is None:
                return await event.bot.send_message(user_handler.id, data["_"]('start.msg.not_profile'))
            
        return await handler(event, data)    

