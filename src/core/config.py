import logging
from pathlib import Path


class Config:
    LOGGING_LEVEL = logging.INFO
    LOGGING_FILE = Path('logs/app.log')
