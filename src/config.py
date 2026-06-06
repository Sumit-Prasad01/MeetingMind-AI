import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")

    SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")

    SARVAM_STT_MODEL = os.getenv("SARVAM_STT_MODEL", "saaras:v2.5")

    SARVAM_STT_TRANSLATE_URL = os.getenv("SARVAM_STT_TRANSLATE_URL")


settings = Settings()