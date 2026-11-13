import os
import logging

from pathlib import Path
from dotenv import load_dotenv


class Config:
    LOGGING_LEVEL = logging.INFO
    LOGGING_FILE = Path('logs/app.log')


class DatabaseVariables:
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DATABASE = os.getenv('DATABASE')
