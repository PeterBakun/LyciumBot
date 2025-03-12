from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import kb
import text
from aiogram import flags
from aiogram.fsm.context import FSMContext
import utils


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name))

@router.message(F.text == "Вибір класу")
@router.message(F.text == "◀️ Вибір класу")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message(Command("profil"))
async def profil(msg: Message):
    await msg.answer(text.clas)
@router.message(Command("8"))
async def eght(msg: Message):
    await msg.answer(text.profil9)
@router.message(Command("9"))
async def neine(msg: Message):
    await msg.answer(text.profil9)
@router.message(Command("10"))
async def ten(msg: Message):
    await msg.answer(text.profil10)
@router.message(Command("cons"))
async def cons(msg: Message):
    await msg.answer(text.cons)
@router.message(Command("test_deta"))
async def test_deta(msg: Message):
    await msg.answer(text.test_deta)
@router.message(Command("docs_deta"))
async def docs_deta(msg: Message):
    await msg.answer(text.docs_deta)
@router.message(Command("test"))
async def test(msg: Message):
    await msg.answer(text.test)
@router.message(Command("docs"))
async def docs(msg: Message):
    await msg.answer(text.docs)
@router.message(Command("result"))
async def result(msg: Message):
    await msg.answer(text.result)

