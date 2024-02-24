import logging
from fastapi import FastAPI
# GETзапросы
#uvicorn lesson.main_02:app --reload

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def read_root():
    logger.info('Отработал GET запрос.')
    return {"Hello": "World"}

