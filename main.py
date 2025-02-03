from fastapi import FastAPI
from routes import health, video, image

app = FastAPI()

app.include_router(health.router, tags=["Health"])
app.include_router(video.router, tags=["Video"])
app.include_router(image.router, tags=["Image"])
