from fastapi import FastAPI, File, UploadFile, BackgroundTasks
import os

from utils import get_file_hash
from db import get_key, set_key, has_key
from processing import turbo, image_to_string

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/video")
async def upload_video(file: UploadFile, background_tasks: BackgroundTasks):
    if file.content_type != "video/mp4":
        return {"error": "Only MP4 files are supported"}
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    file_hash = get_file_hash(file.filename)
    if has_key(file_hash):
        return {"transcription": get_key(file_hash)}
    result = turbo.transcribe(file.filename)
    set_key(file_hash, result["text"])
    background_tasks.add_task(os.remove, file.filename)
    return {"transcription": result["text"]}


@app.post("/image")
async def upload_image(file: UploadFile, background_tasks: BackgroundTasks):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Only JPEG and PNG files are supported"}
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    file_hash = get_file_hash(file.filename)
    if has_key(file_hash):
        return {"transcription": get_key(file_hash)}
    result = image_to_string(file.filename)
    set_key(file_hash, result)
    background_tasks.add_task(os.remove, file.filename)
    return {"transcription": result}
