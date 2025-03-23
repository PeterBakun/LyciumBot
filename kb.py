from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Створення inline-клавіатури
menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Профілі навчання в ліцеї", callback_data="profil"),
     InlineKeyboardButton(text="Консультаційні курси", callback_data="cons")],
    [InlineKeyboardButton(text="Терміни вступних випробувань", callback_data="test_deta"),
     InlineKeyboardButton(text="Терміни прийому документів", callback_data="docs_deta")],
    [InlineKeyboardButton(text="Вступні випробування", callback_data="test"),
     InlineKeyboardButton(text="Документи для вступу", callback_data="docs")],
    [InlineKeyboardButton(text="Коли відбувається зарахування?", callback_data="result"),
     InlineKeyboardButton(text="Контакти ліцею", callback_data="contact")]
])

# Reply-клавіатура (звичайні кнопки, що залишаються на екрані)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Вийти в меню")]], resize_keyboard=True)

# Inline-кнопка для виходу
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Вийти в меню", callback_data="menu")]])

# Клавіатура з вибором класу
class_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="8", callback_data="8"),
     InlineKeyboardButton(text="9", callback_data="9")],
    [InlineKeyboardButton(text="10", callback_data="10")]
])
