from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from ..utils import get_lang, get_lang_strings


router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message, command: CommandObject):
    lang = get_lang(message.from_user)
    strings = get_lang_strings(lang)
    await message.answer(
        strings['start'].format(
            message.from_user.first_name
        )
    )