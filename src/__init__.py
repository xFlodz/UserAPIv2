import logging

from src.core.config import Config

class Logger:
    def __init__(self):
        self.level = Config.LOGGING_LEVEL

    def setup_logger(self):
        logging.basicConfig(
            level=self.level,
            datefmt='%Y-%m-%d %H:%M:%S',
            format='[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s'
        )

logger = Logger()