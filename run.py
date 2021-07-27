from app import app
import os
from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.environ.get("APP_HOST")
APP_PORT = os.environ.get("APP_PORT")

app.run(debug=True, host=APP_HOST, port=APP_PORT)