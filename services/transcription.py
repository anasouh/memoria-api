from db import get_key, set_key, has_key
from utils.files import get_file_hash
from processing.speech import turbo

import os


async def transcribe_video(file_path: str) -> str:
    """Transcrit une vidéo en texte"""
    file_hash = get_file_hash(file_path)

    if has_key(file_hash):
        return get_key(file_hash)

    result = turbo.transcribe(file_path)
    set_key(file_hash, result["text"])

    os.remove(file_path)
    return result["text"]
