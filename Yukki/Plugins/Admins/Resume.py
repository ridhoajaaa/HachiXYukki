import asyncio
import os
import random
from asyncio import QueueEmpty

from telegram import ParseMode
from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)

from config import get_queue
from Yukki import BOT_USERNAME, MUSIC_BOT_NAME, app, db_mem
from Yukki.Core.PyTgCalls import Queues
from Yukki.Core.PyTgCalls.Converter import convert
from Yukki.Core.PyTgCalls.Downloader import download
from Yukki.Core.PyTgCalls.Yukki import (pause_stream, resume_stream,
                                        skip_stream, skip_video_stream,
                                        stop_stream)
from Yukki.Database import (is_active_chat, is_music_playing, music_off,
                            music_on, remove_active_chat,
                            remove_active_video_chat)
from Yukki.Decorators.admins import AdminRightsCheck
from Yukki.Decorators.checker import checker, checkerCB
from Yukki.Inline import audio_markup, primary_markup, secondary_markup2
from Yukki.Utilities.changers import time_to_seconds
from Yukki.Utilities.chat import specialfont_to_normal
from Yukki.Utilities.theme import check_theme
from Yukki.Utilities.thumbnails import gen_thumb
from Yukki.Utilities.timer import start_timer
from Yukki.Utilities.youtube import get_m3u8, get_yt_info_id

loop = asyncio.get_event_loop()


@app.on_message(
    filters.command(["resume", "resu"]) & filters.group
)
@AdminRightsCheck
@checker
async def resume(_, message: Message):
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
    if message.command[0][1] == "e":
        if await is_music_playing(message.chat.id):
            return await message.reply_text("Music Played.")
        await music_on(chat_id)
        await resume_stream(chat_id)
        await message.reply_text(
            f"<b>▶️ Music playback resume by {message.from_user.mention}!</b>\n\n"
            f"× To pause music playing, can use » /pause commands.",
            parse_mode=ParseMode.HTML,
        )
    