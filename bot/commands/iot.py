from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommand

from loader import _, bot, i18n


def get_iot_commands(lang: str = 'en') -> list[BotCommand]:
    commands = [
        BotCommand('/take_picture', _('take picture', locale=lang)),
        BotCommand('/last_move', _('last_move', locale=lang)),
        BotCommand('/status', _('status', locale=lang)),
        BotCommand('/test', _('test', locale=lang)),
    ]

    return commands


async def set_default_commands():
    await bot.set_my_commands(get_iot_commands(), scope=BotCommandScopeDefault())

    for lang in i18n.available_locales:
        await bot.set_my_commands(get_iot_commands(lang), scope=BotCommandScopeDefault(), language_code=lang)


async def set_user_commands(user_id: int, commands_lang: str):
    await bot.set_my_commands(get_iot_commands(commands_lang), scope=BotCommandScopeChat(user_id))
