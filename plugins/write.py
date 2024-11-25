#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from TheApi import api

from DnsXMusic import app


@app.on_message(filters.command(["write"]))
async def write(client, message):
    if message.reply_to_message and message.reply_to_message.text:
        txt = message.reply_to_message.text
    elif len(message.command) > 1:
        txt = message.text.split(None, 1)[1]
    else:
        return await message.reply(
            "Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ᴡʀɪᴛᴇ ᴀғᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴜsᴇ ᴡʀɪᴛᴇ CMD"
        )
    nan = await message.reply_text("Pʀᴏᴄᴇssɪɴɢ...")
    try:
        img = api.write(txt)
        await message.reply_photo(img)
        await nan.delete()
    except Exception as e:
        await nan.edit(e)


__MODULE__ = "Wʀɪᴛᴇ"
__HELP__ = """
**COMMANDS**:
- /write: ᴡʀɪᴛᴇ ᴛᴇxᴛ ᴏɴ ᴀɴ ᴄʟᴏᴜᴅ ᴀɴᴅ ɢᴇᴛ ᴀɴ ᴇᴅɪᴛᴇᴅ ᴘʜᴏᴛᴏ.

**INFO**:
- ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: ᴡʀɪᴛᴇ
- ᴅᴇsᴄʀɪᴘᴛɪᴏɴ: ᴡʀɪᴛᴇ ᴛᴇxᴛ ᴏɴ ᴀɴ ᴄʟᴏᴜᴅ ᴀɴᴅ ɢᴇᴛ ᴀɴ ᴇᴅɪᴛᴇᴅ ᴘʜᴏᴛᴏ.
- ᴄᴏᴍᴍᴀɴᴅs: /write
- ᴘᴇʀᴍɪssɪᴏɴs ɴᴇᴇᴅᴇᴅ: ɴᴏɴᴇ

**NOTE**:
- ᴜsᴇ ᴅɪʀᴇᴄᴛʟʏ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ ғᴏʀ ᴛʜᴇ ʙᴇsᴛ ʀᴇsᴜʟᴛs."""
