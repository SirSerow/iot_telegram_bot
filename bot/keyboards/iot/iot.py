
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from loader import _


def get_iot_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(_('Take picture'), _('Last move'))
    markup.add(_('Status'), _('Test'))

    return markup
