import uvicorn
from fastapi import FastAPI

from src.core.logging import logger_config

logger_config.setup()
app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)


