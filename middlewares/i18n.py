from typing import Any, Awaitable, Callable
from aiogram.types import TelegramObject, User
from aiogram import BaseMiddleware
from db.database import DataBase
from utils.i18n import i18n
from global_data import global_context

class I18nMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any]
    ) -> Any:
        user_handler: User | None = data.get("event_from_user")
        locale = 'ru'
        if user_handler:
            db: DataBase = global_context.get()
            user_db = db.get_user(user_handler.id)
            if user_db:
                locale = user_db['language']

        def _(key:str, lc=locale) -> str:
            if lc == None:
                return i18n.get(locale,key)
            return i18n.get(lc, key)
        
        data["_"] = _
        data["locale"] = locale

        return await handler(event, data)
