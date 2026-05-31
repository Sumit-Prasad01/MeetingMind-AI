import os
from dotenv import load_dotenv

class Settings:

    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")



settings = Settings()