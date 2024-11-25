#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.

import requests
from pyrogram import filters

from DnsXMusic import app
from SafoneAPI import SafoneAPI


@app.on_message(filters.command(["bard"]))
async def bard(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Example:\n\n`/bard tell me about lord rama and sita in brief `"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    try:
        Z = await SafoneAPI().bard(user_input)
        result = Z["candidates"][0]["content"]["parts"][0]["text"]
        await message.reply_text(result)
    except requests.exceptions.RequestException as e:
        pass
