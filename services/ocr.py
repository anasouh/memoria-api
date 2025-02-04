from db import get_key, set_key, has_key
from utils.files import get_file_hash
import os
from processing.ocr import image_to_string


async def extract_text_from_image(file_path: str) -> str:
    """Effectue l'OCR sur une image"""
    file_hash = get_file_hash(file_path)

    if has_key(file_hash):
        return get_key(file_hash)

    text = image_to_string(file_path)
    text = text.replace("\n", " ")
    set_key(file_hash, text)

    os.remove(file_path)
    return text
