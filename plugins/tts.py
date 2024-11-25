#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.

import io

from gtts import gTTS
from pyrogram import filters

from DnsXMusic import app


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Please provide some text to convert to speech."
        )

    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang="hi")
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    audio_file = io.BytesIO(audio_data.read())
    audio_file.name = "audio.mp3"
    await message.reply_audio(audio_file)


__HELP__ = """
**ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ**

ᴜsᴇ ᴛʜᴇ `/tts` ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ɪɴᴛᴏ sᴘᴇᴇᴄʜ.

- `/tts <ᴛᴇxᴛ>`: ᴄᴏɴᴠᴇʀᴛs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ɪɴ ʜɪɴᴅɪ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/tts Namaste Duniya`

**ɴᴏᴛᴇ:**
ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴀғᴛᴇʀ ᴛʜᴇ `/tts` ᴄᴏᴍᴍᴀɴᴅ.
"""

__MODULE__ = "Tᴛs"
