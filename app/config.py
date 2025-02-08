from dotenv import load_dotenv
import os
from pathlib import Path
import sys

class Settings:
    BASE_DIR = Path(__file__).resolve().parent.parent
    ENV_PATH = BASE_DIR / ".env"
    load_dotenv(ENV_PATH)

    def __init__(self):
        # DB Production
        self.DB_URL = os.getenv('DB_URL')

        if not self.DB_URL:
            print("ERROR: La variable de entorno DB_URL no está definida.")
            print("La aplicación no puede iniciarse.")
            sys.exit(1)

settings = Settings()