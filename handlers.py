from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import kb
import text
from aiogram import flags
from aiogram.fsm.context import FSMContext
import utils
import database
from states import UserState


router = Router()


@router.callback_query(F.data.in_(["8", "9", "10"]))
async def select_class(call: CallbackQuery, state: FSMContext):
    selected_class = call.data  # Отримуємо вибраний клас
    user_id = call.from_user.id
    username = call.from_user.username

    await state.update_data(selected_class=selected_class)

    database.save_user(user_id, username, selected_class)

    await call.message.answer(f"✅ Ви обрали {selected_class} клас!", reply_markup=kb.menu)
    await call.answer()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(
        f"Привіт {message.from_user.first_name}👋, цей бот допоможе Вам дізнатись інформацію про вступ до Наукового ліцею «Політ». Виберіть клас в який ви вступаєте:",
        reply_markup=kb.class_kb  # Кнопки вибору класу
    )
    await state.set_state(UserState.selected_class)

@router.message(F.text == "Вибір класу")
@router.message(F.text == "◀️ Вибір класу")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message(F.text == "Консультаційні курси")
async def cons(msg: Message):
    await msg.answer(text.cons)

# 🔹 Хендлери для inline-кнопок (callback_data)
@router.callback_query(F.data == "profil")
async def callback_profil(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    selected_class = user_data.get("selected_class", None)

    if selected_class == "8":
        await call.message.answer(text.profil8)
    elif selected_class == "9":
        await call.message.answer(text.profil9)
    elif selected_class == "10":
        await call.message.answer(text.profil10)
    else:
        await call.message.answer("⚠️ Ви ще не вибрали клас! Будь ласка, виберіть клас спочатку.")

    await call.answer()

@router.callback_query(F.data == "cons")
async def callback_cons(call: CallbackQuery):
    await call.message.answer(text.cons)
    await call.answer()

@router.callback_query(F.data == "test_deta")
async def callback_test_deta(call: CallbackQuery):
    await call.message.answer(text.test_deta)
    await call.answer()

@router.callback_query(F.data == "docs_deta")
async def callback_docs_deta(call: CallbackQuery):
    await call.message.answer(text.docs_deta)
    await call.answer()

@router.callback_query(F.data == "test")
async def callback_test(call: CallbackQuery):
    await call.message.answer(text.test)
    await call.answer()

@router.callback_query(F.data == "docs")
async def callback_docs(call: CallbackQuery):
    await call.message.answer(text.docs)
    await call.answer()

@router.callback_query(F.data == "result")
async def callback_result(call: CallbackQuery):
    await call.message.answer(text.result)
    await call.answer()

@router.callback_query(F.data == "contact")
async def callback_result(call: CallbackQuery):
    await call.message.answer(text.contact)
    await call.answer()