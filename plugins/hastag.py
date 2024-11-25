#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from DnsXMusic import app
from TheApi import api


@app.on_message(filters.command("hastag"))
async def hastag(bot, message):

    try:
        text = message.text.split(" ", 1)[1]
        res = api.gen_hashtag(text)
    except IndexError:
        return await message.reply_text("Example:\n\n/hastag python")

    await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ  ʜᴀsᴛᴀɢ :\n<pre>{res}</pre>", quote=True)


__MODULE__ = "Hᴀsʜᴛᴀɢ"
__HELP__ = """
**ʜᴀsʜᴛᴀɢ ɢᴇɴᴇʀᴀᴛᴏʀ:**

• `/hashtag [text]`: Gᴇɴᴇʀᴀᴛᴇ ʜᴀsʜᴛᴀɢs ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
