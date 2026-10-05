from aiogram import Router, types, F
from aiogram.enums import ParseMode
from db.database import DataBase
from keyboards.inline import InlinrKeyboard
from global_data import global_context
from states.movie import MovieForm
from states.profile import Profile
from aiogram.fsm.context import FSMContext
from config import API_OMDB
from services.api import APIReqest 

router = Router()

@router.message((F.text == "Профиль") | (F.text == "Обліковий запис") | (F.text == "Profile"))
async def check_text(message: types.Message, _):
    db: DataBase = global_context.get()
    find_user = db.get_user(message.from_user.id)
    await message.answer(f'<b>{_("profile.msg.name")}:</b> <i>{find_user["full_name"]}</i>\n'
                         f'<b>{_("profile.msg.username")}:</b> <i>{find_user["username"]}</i>\n'
                         f'<b>{_("profile.msg.id")}:</b> <i>{find_user["user_id"]}</i>\n'
                         f'<b>{_("profile.msg.language")}:</b> <i>{find_user["language"]}</i>', parse_mode=ParseMode.HTML, reply_markup=InlinrKeyboard.profil_keyboard(_))
        
@router.message((F.text == "Поиск") | (F.text == "Пошук") | (F.text == "Search"))
async def check_text(message: types.Message, _):
    await message.answer(f'{_("search.msg.what_search")}', reply_markup=InlinrKeyboard.choose_film_series(_))


@router.message(MovieForm.title)
async def get_title(message: types.Message, state: FSMContext, _):
    user_search = message.text
    db: DataBase = global_context.get()
    db.add_history(user_search, db.get_user(message.from_user.id)["id"])
    type = (await state.get_data())['type']
    await message.answer(f"{_('search.msg.search_film')} {user_search} ...")
    films = APIReqest.search(user_search, type)
    if films['Response'] == 'True':
        await message.answer(f"{_('search.msg.result')}", reply_markup=InlinrKeyboard.films(films))
    else:
        await message.answer(f"{_('search.msg.no_result')}")

@router.message(Profile.full_name)
async def change_full_name(message: types.Message, _):
    new_full_name = message.text
    db: DataBase = global_context.get()
    db.change_full_name(message.from_user.id, new_full_name)
    await message.answer(f"{_('change_profile.msg.update_profile')}")

@router.message(Profile.username)
async def change_username(message: types.Message, _):
    new_username = message.text
    db: DataBase = global_context.get()
    db.change_username(message.from_user.id, new_username)
    await message.answer(f"{_('change_profile.msg.update_profile')}")