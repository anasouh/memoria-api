from fastapi import APIRouter, UploadFile

from services.transcription import transcribe_video
from utils.files import save_temp_file

router = APIRouter()


@router.post("/video")
async def upload_video(file: UploadFile):
    if file.content_type != "video/mp4":
        return {"error": "Only MP4 files are supported"}

    file_path = save_temp_file(file)
    transcription = await transcribe_video(file_path)
    return {"transcription": transcription}
