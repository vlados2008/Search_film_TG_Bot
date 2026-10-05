from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from db.database import DataBase
from services.user import User
from keyboards.reply import ReplyKeyboard
from global_data import global_context


router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message, _):
    db: DataBase = global_context.get()
    find_user = db.get_user(message.from_user.id)
    if find_user is None:
        user = User.create_from_message(message)
        db.add_user(user)   
        await message.answer(f'{_("start.msg.welcome")} <b><i>{user.username}</i></b>!', parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboard.main_keyboard(_))
    else:
        await message.answer(f'{_("start.msg.restart")} <b><i>{find_user["username"]}</i></b>!', parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboard.main_keyboard(_))