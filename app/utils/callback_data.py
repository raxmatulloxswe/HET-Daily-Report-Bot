from enum import Enum
from aiogram.filters.callback_data import CallbackData


class MainMenuAction(str, Enum):
    ORDER = 'order'
    ABOUT = 'about'
    MY_ORDERS = 'my_orders'
    BRANCHES = 'branches'
    SETTINGS = 'settings'


class MainMenuCallbackData(CallbackData, prefix='main_menu'):
    action: MainMenuAction


def cb_main_menu_callback_data(action):
    return MainMenuCallbackData(action=action.value).pack()


class BackToMainMenuAction(str, Enum):
    BACK = 'back'


class BackToMainMenuCallbackData(CallbackData, prefix='back_main_menu'):
    action: BackToMainMenuAction


def cb_back_to_main_menu_callback_data():
    return BackToMainMenuCallbackData(action=BackToMainMenuAction.BACK.value).pack()


class SelectLanguage(str, Enum):
    UZ = 'uz'
    RU = 'ru'
    EN = 'en'


class SelectLanguageCallbackData(CallbackData, prefix='select_language'):
    language: SelectLanguage


def cb_select_language_callback_data(lang):
    return SelectLanguageCallbackData(language=lang.value).pack()
