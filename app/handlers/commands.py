from aiogram import Router, types, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommand
from app.keyboards.inline import inline_main_menu


router = Router()


@router.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer("Assalomu Alekum!\n\n Siz Elektrning kunlik hisobotini har kuni olib turmoqchimisiz? \n\n Bu <b>Rasmiy</b> bot emas!", reply_markup=inline_main_menu())


@router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("Available commands:\n/start - Start the bot\n/help - Get help")


@router.message(Command('check_state'))
async def check_state(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await message.answer(f"State: {current_state}")


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish!"),
        BotCommand(command="help", description="Yordam haqida ma'lumot!"),
        BotCommand(command="check_state", description="Qaysi stateda ekanligini ko'rsatadi!"),
    ]
    await bot.set_my_commands(commands)