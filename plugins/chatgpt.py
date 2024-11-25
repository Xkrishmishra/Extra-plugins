#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.enums import ChatAction
from TheApi import api

from DnsXMusic import app
from config import BANNED_USERS


@app.on_message(filters.command(["chatgpt", "ai", "ask"]) & ~BANNED_USERS)
async def chatgpt_chat(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Example:\n\n`/ai write simple website code using html css, js?`"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    results = api.chatgpt(user_input)
    await message.reply_text(results)


__MODULE__ = "CʜᴀᴛGᴘᴛ"
__HELP__ = """
/advice - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ ʙʏ ʙᴏᴛ
/ai [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ's ᴀɪ
/gemini [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ɢᴇᴍɪɴɪ ᴀɪ
/bard [ǫᴜᴇʀʏ] -ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ʙᴀʀᴅ ᴀɪ"""
