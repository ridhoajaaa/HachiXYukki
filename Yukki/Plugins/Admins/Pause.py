#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from Yukki.Decorators.checker import checker
from telegram import ParseMode
from pyrogram import filters
from pyrogram.types import Message

from Yukki import app
from Yukki.Core.PyTgCalls.Yukki import pause_stream
from Yukki.Database import is_music_playing, music_off, is_active_chat
from Yukki.Decorators.admins import AdminRightsCheck


@app.on_message(
    filters.command(["pause", "paus"]) & filters.group
)
@AdminRightsCheck
@checker
async def pause_admin(_, message: Message):
    global get_queue
    if not len(message.command) == 1:
        return await message.reply_text("Error! Wrong Usage of Command.")
    if not await is_active_chat(message.chat.id):
        return await message.reply_text(
        f"<u><b>Voice Chat Not Found</b></u>\n"
        f"Nothing plays in voice chat.  Active Voice Chat Not Found",
        parse_mode=ParseMode.HTML,
        )
    chat_id = message.chat.id
    if not len(message.command) == 1:
        return await message.edit_text("Error! Wrong Usage of Command.")
    if message.command[0][1] == "a":
        if not await is_music_playing(chat_id):
            return await message.edit_text("Music is already Paused.")
    await music_off(chat_id)
    await pause_stream(chat_id)
    await message.edit_text(
        f"<b>⏸ Music playback paused by {message.from_user.mention}!</b>\n\n"
        f"× To resume music playing, can use » /resume commands.",
        parse_mode=ParseMode.HTML,
    )
    
