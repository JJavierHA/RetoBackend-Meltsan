from dotenv import load_dotenv
import os
from pathlib import Path

class Settings:
    BASE_DIR = Path(__file__).resolve().parent.parent
    ENV_PATH = BASE_DIR / ".env"
    load_dotenv(ENV_PATH)

    def __init__(self):
        # DB Production
        self.DB_URL = os.getenv('DB_URL')

settings = Settings()