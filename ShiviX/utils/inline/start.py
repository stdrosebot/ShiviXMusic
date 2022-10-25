from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from ShiviX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 Add Me To Your Group 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Help",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Settings", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Maintainer", user_id=OWNER),
            InlineKeyboardButton(
                text="Support", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me Else You Gey",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Help", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", callback_data="cb_about")
        ],
        [
            InlineKeyboardButton(
                text="Channel", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Support", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="Source", url=f"https://telegra.ph/file/9b0455dae14d5639f936d.mp4"
            ),
            InlineKeyboardButton(text="Maintainer", user_id=OWNER)
        ],
     ]
    return buttons
