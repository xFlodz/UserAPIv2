import uvicorn
import logging
from fastapi import FastAPI

from src.core.logging_configuration import logger_config
from src.api import router

logger_config.setup()
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    logger.info('Сервер запущен')
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)


