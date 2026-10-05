from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from keyboards.inline import InlinrKeyboard
from keyboards.reply import ReplyKeyboard
from db.database import DataBase
from aiogram.enums import ParseMode
from global_data import global_context
from states.movie import MovieForm
from states.profile import Profile
from config import API_OMDB
from services.api import APIReqest 
from utils.formater import formater

router = Router()

@router.callback_query(F.data == "change_profil")
async def change_profil(callback:types.CallbackQuery, _):
    await callback.message.answer(f'{_("change_profile.msg.question")}', reply_markup=InlinrKeyboard.change_profil_keyboard(_))

@router.callback_query(F.data == "change_language")
async def change_language(callback:types.CallbackQuery, _):
    await callback.message.answer(f'{_("change_lang.msg.action_change")}', reply_markup=InlinrKeyboard.language_keyboard(_))

@router.callback_query(F.data == "delete_profile")
async def delate_profile(callback:types.CallbackQuery, _):
    db: DataBase = global_context.get()
    db.delete_user(callback.from_user.id)
    await callback.answer(f'{_("delete_profile.msg")}')

@router.callback_query((F.data == "ru") | (F.data == "uk") | (F.data == "en"))
async def change_lang(callback: types.CallbackQuery, _):
    lang = callback.data
    db: DataBase = global_context.get()
    db.change_lang(callback.from_user.id, lang)
    await callback.message.edit_text(
        text = f"{_('change_lang.msg.action_change', lang)}", reply_markup=InlinrKeyboard.language_keyboard(_, lang)
    )
    await callback.message.answer(f"{_('change_lang.msg.info_change', lang)}", reply_markup=ReplyKeyboard.main_keyboard(_, lang))

@router.callback_query((F.data == "film") | (F.data == "series"))
async def select_type_search(callback: types.CallbackQuery, state: FSMContext, _):
    await state.set_state(MovieForm.title)
    if callback.data == "film":
        await state.update_data(type='movie')
        await callback.message.answer(f"<b>{_('search.msg.enter_name_film')}</b>", parse_mode=ParseMode.HTML)
    else:
        await state.update_data(type='series')
        await callback.message.answer(f"<b>{_('search.msg.enter_name_series')}</b>", parse_mode=ParseMode.HTML)

@router.callback_query(F.data.startswith("film_"))
async def detail_film(callback: types.CallbackQuery, _):
    id = callback.data.split("_")[1]
    film_descr = APIReqest.info_film(id)

    await callback.message.answer_photo(photo=f"{film_descr['Poster']}", caption=f"{_('film.name')} {film_descr['Title']}\n{_('film.released')} {film_descr['Released']}\n{_('film.genre')} {film_descr['Genre']}\n{_('film.runtime')} {film_descr['Runtime']}\n{_('film.country')} {film_descr['Country']}\n{_('film.plot')} {formater(film_descr['Plot'])}")

@router.callback_query(F.data == "full_name")
async def name(callback: types.CallbackQuery, state: FSMContext, _):
    await callback.message.answer(f"{_('change_profile.msg.new_name')}")
    await state.set_state(Profile.full_name)

@router.callback_query(F.data == "username")
async def username(callback: types.CallbackQuery, state: FSMContext, _):
    await callback.message.answer(f"{_('change_profile.msg.new_username')}")
    await state.set_state(Profile.username)

@router.callback_query(F.data == "get_history")
async def history_callback(callback: types.CallbackQuery, state: FSMContext, _):
    db: DataBase = global_context.get()
    histories = db.get_history(callback.from_user.id)
    text_histories = f"<b>{_('profile.btns.history')}</b>:\n"
    num = 0
    for history in histories:
        num += 1
        text_histories += f"<b>{num}.</b> {history['name']}\n"
    await callback.message.answer(f'{text_histories}', parse_mode=ParseMode.HTML)