import uvicorn
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.core.logging_configuration import logger_config
from src.core.database import create_tables
from src.api import router

logger_config.setup()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)

if __name__ == '__main__':
    logger.info('Сервер запущен')
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)


