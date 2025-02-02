from fastapi import FastAPI, File, UploadFile, BackgroundTasks
import whisper, pytesseract, os

app = FastAPI()
model = whisper.load_model("turbo")


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
    result = model.transcribe(file.filename)
    background_tasks.add_task(os.remove, file.filename)
    return {"transcription": result}


@app.post("/image")
async def upload_image(file: UploadFile, background_tasks: BackgroundTasks):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Only JPEG and PNG files are supported"}
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    result = pytesseract.image_to_string(file.filename)
    background_tasks.add_task(os.remove, file.filename)
    return {"transcription": result}
