from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Jazz",
                callback_data=f"play_playlist {user_id}|{type}|Jazz",
            ),
            InlineKeyboardButton(
                text=f"Dangdut",
                callback_data=f"play_playlist {user_id}|{type}|Dangdut",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"DJ",
                callback_data=f"play_playlist {user_id}|{type}|DJ",
            ),
            InlineKeyboardButton(
                text=f"Lofi",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Sad",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"Rock",
                callback_data=f"play_playlist {user_id}|{type}|Rock",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Gustixa",
                callback_data=f"play_playlist {user_id}|{type}|Gustixa",
            ),
            InlineKeyboardButton(
                text=f"Others",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ Rock",
                callback_data=f"add_playlist {videoid}|{type}|Rock",
            ),
            InlineKeyboardButton(
                text=f"✚ Sad",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ DJ",
                callback_data=f"add_playlist {videoid}|{type}|DJ",
            ),
            InlineKeyboardButton(
                text=f"✚ Lofi",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Jazz",
                callback_data=f"add_playlist {videoid}|{type}|Jazz",
            ),
            InlineKeyboardButton(
                text=f"✚ Dangdut",
                callback_data=f"add_playlist {videoid}|{type}|Dangdut",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Gustixa",
                callback_data=f"add_playlist {videoid}|{type}|Gustixa",
            ),
            InlineKeyboardButton(
                text=f"✚ Others",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Rock", callback_data=f"check_playlist {type}|Rock"
            ),
            InlineKeyboardButton(
                text=f"Sad", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"DJ", callback_data=f"check_playlist {type}|DJ"
            ),
            InlineKeyboardButton(
                text=f"Lofi", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Jazz",
                callback_data=f"check_playlist {type}|Jazz",
            ),
            InlineKeyboardButton(
                text=f"Dangdut",
                callback_data=f"check_playlist {type}|Dangdut",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Gustixa",
                callback_data=f"check_playlist {type}|Gustixa",
            ),
            InlineKeyboardButton(
                text=f"Others", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Close", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="❚❚", callback_data=f"pausecb"),
            InlineKeyboardButton(text="☳", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Checkout Queued Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Close Menu", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
    ]
    return buttons
