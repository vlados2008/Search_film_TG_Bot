from aiogram.utils.keyboard import ReplyKeyboardBuilder

class ReplyKeyboard:
    @staticmethod
    def main_keyboard(_, lang=None):
        kb = ReplyKeyboardBuilder()
        kb.button(text=f'{_("start.btns.search", lang)}')
        kb.button(text=f'{_("start.btns.profile", lang)}')
        kb.adjust(1)
        keyboard = kb.as_markup(resize_keyboard=True)
        return keyboard
