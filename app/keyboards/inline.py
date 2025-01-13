from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.utils.callback_data import cb_main_menu_callback_data, MainMenuAction, cb_back_to_main_menu_callback_data, \
    cb_select_language_callback_data, SelectLanguage


def inline_back_to_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Asosiy menu', callback_data=cb_back_to_main_menu_callback_data())
    return inline_keyboard.as_markup()


def inline_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Mening Hisobim!',
                           callback_data=cb_main_menu_callback_data(action=MainMenuAction.ORDER))
    inline_keyboard.button(text='Yangi hisob qo`shish', callback_data=cb_main_menu_callback_data(action=MainMenuAction.ABOUT))

    inline_keyboard.adjust(1)
    return inline_keyboard.as_markup()


def inline_languages():
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='Uzbek', callback_data=cb_select_language_callback_data(lang=SelectLanguage.UZ))
    inline_keyboard.button(text='Russian', callback_data=cb_select_language_callback_data(lang=SelectLanguage.RU))
    inline_keyboard.button(text='English', callback_data=cb_select_language_callback_data(lang=SelectLanguage.EN))

    inline_keyboard.adjust(1)
    return inline_keyboard.as_markup()
