from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")

config_obj = Config()

