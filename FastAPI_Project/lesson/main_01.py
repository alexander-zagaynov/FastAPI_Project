from fastapi import FastAPI

app = FastAPI()
#uvicorn lesson.main_01:app --reload


@app.get('/')
async def root():
    return{'message': "Hello Word"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}