from fastapi import APIRouter, UploadFile

from services.ocr import extract_text_from_image
from utils.files import save_temp_file

router = APIRouter()


@router.post("/image")
async def upload_image(file: UploadFile):
    if not file.content_type.startswith("image/"):
        return {"error": "Only image files are supported"}

    file_path = save_temp_file(file)
    transcription = await extract_text_from_image(file_path)
    return {"transcription": transcription}
