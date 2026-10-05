from aiogram.utils.keyboard import InlineKeyboardBuilder

class InlinrKeyboard:
    @staticmethod
    def profil_keyboard(_, lang=None):
        kb = InlineKeyboardBuilder()

        kb.button(text=f'{_("profile.btns.change_profile", lang)}', callback_data='change_profil')
        kb.button(text=f'{_("profile.btns.change_lang", lang)}', callback_data='change_language')
        kb.button(text=f'{_("profile.btns.history", lang)}', callback_data='get_history')
        kb.button(text=f'{_("profile.btns.delete_profile", lang)}', callback_data='delete_profile')

        kb.adjust(2, 1, 1)
        keyboard = kb.as_markup()
        return keyboard
    
    @staticmethod
    def language_keyboard(_, lang=None):
        kb = InlineKeyboardBuilder()

        kb.button(text=f'{_("change_lang.btns.ru", lang)}', callback_data='ru')
        kb.button(text=f'{_("change_lang.btns.uk", lang)}', callback_data='uk')
        kb.button(text=f'{_("change_lang.btns.en", lang)}', callback_data='en')

        kb.adjust(3)
        keyboard = kb.as_markup()
        return keyboard
    
    @staticmethod
    def change_profil_keyboard(_, lang=None):
        kb = InlineKeyboardBuilder()

        kb.button(text=f'{_("change_profile.btns.name", lang)}', callback_data='full_name')
        kb.button(text=f'{_("change_profile.btns.username", lang)}', callback_data='username')

        kb.adjust(2)
        keyboard = kb.as_markup()
        return keyboard
    
    @staticmethod
    def choose_film_series(_, lang=None):
        kb = InlineKeyboardBuilder()

        kb.button(text=f'{_("search.btns.film", lang)}', callback_data="film")
        kb.button(text=f'{_("search.btns.series", lang)}', callback_data="series")

        kb.adjust(2)
        keyboard = kb.as_markup()
        return keyboard
    
    @staticmethod
    def films(films):
        kb = InlineKeyboardBuilder()
        for film in films['Search']:
            kb.button(text=f"{film['Title']}", callback_data=f"film_{film['imdbID']}")

        kb.adjust(2)
        keyboard = kb.as_markup()
        return keyboard