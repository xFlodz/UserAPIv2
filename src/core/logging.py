import logging
import sys

from src.core.config  import Config

class Logger:
    def __init__(self):
        self.level = Config.LOGGING_LEVEL
        self.datefmt = '%Y-%m-%d %H:%M:%S'
        self.format = '[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s'

    def setup(self):
        formatter = logging.Formatter(
            fmt=self.format,
            datefmt=self.datefmt,
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(self.level)

        logger = logging.getLogger(__name__)
        logger.addHandler(console_handler)

logger_config = Logger()

