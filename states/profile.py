from aiogram.fsm.state import State, StatesGroup

class Profile(StatesGroup):
    full_name = State()
    username = State()