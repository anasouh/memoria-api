import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    REDIS_HOST = os.getenv("REDIS_URL", "localhost")
    REDIS_DB = os.getenv("REDIS_DB", 0)
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)


settings = Settings()
