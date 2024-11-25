#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.enums import ChatType, ParseMode
from pyrogram.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from DnsXMusic import app
from DnsXMusic.utils.functions import MARKDOWN


@app.on_message(command("markdownhelp"))
async def mkdwnhelp(_, m: Message):
    keyb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Click Here!",
                    url=f"http://t.me/{app.username}?start=mkdwn_help",
                )
            ]
        ]
    )
    if m.chat.type != ChatType.PRIVATE:
        await m.reply(
            "Click on the below button to get markdown usage syntax in pm!",
            reply_markup=keyb,
        )
    else:
        await m.reply(
            MARKDOWN, parse_mode=ParseMode.HTML, disable_web_page_preview=True
        )
    return
