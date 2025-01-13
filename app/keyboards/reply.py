from aiogram.utils.keyboard import ReplyKeyboardBuilder



def reply_start_order():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Eltib berish")
    reply_keyboard.button(text="Borib olish")
    reply_keyboard.button(text="Orqaga")

    reply_keyboard.adjust(2)

    return reply_keyboard.as_markup(resize_keyboard=True)
