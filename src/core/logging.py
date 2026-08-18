import logging
from src.core.config  import Config

class Logger:
    def __init__(self):
        self.level = Config.LOGGING_LEVEL
        self.datefmt = '%Y-%m-%d %H:%M:%S'
        self.format = '[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)10s - %(message)s'

    def setup(self):
        logging.basicConfig(
            level=self.level,
            datefmt=self.datefmt,
            format=self.format,
        )

logger_config = Logger()

