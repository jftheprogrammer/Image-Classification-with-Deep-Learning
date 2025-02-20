import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./image_classifier.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/image_classifier.h5")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()