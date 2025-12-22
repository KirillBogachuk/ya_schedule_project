import os
from dotenv import load_dotenv

from app import Application

load_dotenv()

API_KEY = os.getenv("API_KEY")


app = Application(API_KEY)

while True:
    app.show_menu()