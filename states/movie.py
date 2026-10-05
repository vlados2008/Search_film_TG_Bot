from aiogram.fsm.state import State, StatesGroup

class MovieForm(StatesGroup):
    title = State()
    type = State()
    