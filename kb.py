from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Профілі навчання в ліцеї", callback_data="profil"),
    InlineKeyboardButton(text="Консультаційні курси", callback_data="cons")],
    [InlineKeyboardButton(text="Терміни вступних випробувань", callback_data="test_deta"),
    InlineKeyboardButton(text="Терміни прийому документів", callback_data="docs_deta")],
    [InlineKeyboardButton(text="Вступні випробування", callback_data="test"),
    InlineKeyboardButton(text="Документи для вступу", callback_data="docs")],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
eight = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="8")]], resize_keyboard=True)

class_ = [
    [InlineKeyboardButton(text="8", callback_data="8"),
    InlineKeyboardButton(text="9", callback_data="9")],
    [InlineKeyboardButton(text="10", callback_data="10")]
]