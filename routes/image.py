from fastapi import APIRouter, UploadFile

from services.ocr import extract_text_from_image
from utils.files import save_temp_file

router = APIRouter()


@router.post("/image")
async def upload_image(file: UploadFile):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Only JPEG and PNG files are supported"}

    file_path = save_temp_file(file)
    transcription = await extract_text_from_image(file_path)
    return {"transcription": transcription}
