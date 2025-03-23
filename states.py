from aiogram.fsm.state import State, StatesGroup

class UserState(StatesGroup):
    selected_class = State()  # Стан для вибору класу