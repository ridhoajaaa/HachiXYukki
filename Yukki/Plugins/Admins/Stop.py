# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from Yukki.Database.queue import is_active_chat
from pyrogram import filters
from pyrogram.types import Message
from telegram import ParseMode

from Yukki import app
from Yukki.Decorators.admins import AdminRightsCheck
from Yukki.Core.PyTgCalls.Yukki import (pause_stream, resume_stream,
                                        skip_stream, skip_video_stream,
                                        stop_stream)


@app.on_message(
    filters.command("end", "stop") & filters.group
)
@AdminRightsCheck
async def admins(cli, message: Message, _, mystic, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text("Error! Wrong Usage of Command.")
    if not await is_active_chat(message.chat.id):
        return await message.reply_text(
        f"<u><b>Voice Chat Not Found</b></u>\n"
        f"Nothing plays in voice chat.  Active Voice Chat Not Found",
        parse_mode=ParseMode.HTML,
        )
    await stop_stream(chat_id)
    await mystic.edit_text(
        f"✅ **Succsesfully ended music, bot dissconnect from voice chat**.",
    )