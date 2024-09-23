from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YTMUSIC import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text="• ʙᴀᴄᴋ •",
            callback_data=f"settingsback_helper",
        ),
       
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• ᴀᴅᴍɪɴ •",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="• ʙᴏᴛ •",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ᴘ-ʟɪsᴛ •",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="• ᴘʟᴀʏ •",
                    callback_data="help_callback hb9",
                ),
            ], 
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="↺ ʙᴧᴄᴋ ↻",
                    callback_data=f"ubot_cb",
                ),
                InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close"),
            ],
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴏᴘᴇɴ ɪɴ ᴘʀɪᴠɪᴛᴇ •", url=f"https://t.me/{app.username}?start=help"
            ),
        ],
    ]
    return buttons
