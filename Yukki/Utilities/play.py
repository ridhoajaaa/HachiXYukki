#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if (
                "vid_" not in rem
                or "live_" not in rem
                or "index_" not in rem
            ):
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass


def track_markup(_, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["🎵 Play Audio"],
                callback_data=f"MusicStream {videoid}|{user_id}|a",
            ),
            InlineKeyboardButton(
                text=_["🎥 Play Video"],
                callback_data=f"MusicStream {videoid}|{user_id}|v",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["close"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["Playlists"],
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text=_["Additional"], switch_inline_query_current_chat=""
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["Close Menu"], callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["Additional"], switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(
                text=_["Close Menu"], callback_data="close"
            ),
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["🎵 Play Audio"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|a",
            ),
            InlineKeyboardButton(
                text=_["🎥 Play Video"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|v",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["close"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["🏮 Start Live Stream"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}",
            ),
            InlineKeyboardButton(
                text=_["Close Menu"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["🎵 Play Audio"],
                callback_data=f"MusicStream {videoid}|{user_id}|a",
            ),
            InlineKeyboardButton(
                text=_["🎥 Play Video"],
                callback_data=f"MusicStream {videoid}|{user_id}|v",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text=_["close"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
    ]
    return buttons
