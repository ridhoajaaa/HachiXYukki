from typing import Dict, List, Union

from Yukki import db

playlistdb_lofi = db.playlistlofi
playlistdb_rock = db.playlistrock
playlistdb_sad = db.playlistsad
playlistdb_DJ = db.playlistDJ
playlistdb_Jazz = db.playlistJazz
playlistdb_Dangdut = db.playlistDangdut
playlistdb_Gustixa = db.playlistGustixa
playlistdb_others = db.playlistothers


async def _get_playlists(chat_id: int, type: str) -> Dict[str, int]:
    if type == "Lofi":
        xd = playlistdb_lofi
    elif type == "Rock":
        xd = playlistdb_rock
    elif type == "Sad":
        xd = playlistdb_sad
    elif type == "DJ":
        xd = playlistdb_DJ
    elif type == "Jazz":
        xd = playlistdb_Jazz
    elif type == "Dangdut":
        xd = playlistdb_Dangdut
    elif type == "Gustixa":
        xd = playlistdb_Gustixa
    elif type == "Others":
        xd = playlistdb_others
    _notes = await xd.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_playlist_names(chat_id: int, type: str) -> List[str]:
    _notes = []
    for note in await _get_playlists(chat_id, type):
        _notes.append(note)
    return _notes


async def get_playlist(
    chat_id: int, name: str, type: str
) -> Union[bool, dict]:
    name = name
    _notes = await _get_playlists(chat_id, type)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_playlist(chat_id: int, name: str, note: dict, type: str):
    name = name
    _notes = await _get_playlists(chat_id, type)
    _notes[name] = note
    if type == "Lofi":
        xd = playlistdb_lofi
    elif type == "Rock":
        xd = playlistdb_rock
    elif type == "Sad":
        xd = playlistdb_sad
    elif type == "DJ":
        xd = playlistdb_DJ
    elif type == "Jazz":
        xd = playlistdb_Jazz
    elif type == "Dangdut":
        xd = playlistdb_Dangdut
    elif type == "Gustixa":
        xd = playlistdb_Gustixa
    elif type == "Others":
        xd = playlistdb_others
    await xd.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_playlist(chat_id: int, name: str, type: str) -> bool:
    notesd = await _get_playlists(chat_id, type)
    name = name
    if type == "Lofi":
        xd = playlistdb_lofi
    elif type == "Rock":
        xd = playlistdb_rock
    elif type == "Sad":
        xd = playlistdb_sad
    elif type == "DJ":
        xd = playlistdb_DJ
    elif type == "Jazz":
        xd = playlistdb_Jazz
    elif type == "Dangdut":
        xd = playlistdb_Dangdut
    elif type == "Gustixa":
        xd = playlistdb_Gustixa
    elif type == "Others":
        xd = playlistdb_others
    if name in notesd:
        del notesd[name]
        await xd.update_one(
            {"chat_id": chat_id}, {"$set": {"notes": notesd}}, upsert=True
        )
        return True
    return False
