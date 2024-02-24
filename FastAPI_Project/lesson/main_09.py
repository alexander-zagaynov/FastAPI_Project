from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
#uvicorn lesson.main_09:app --reload

app = FastAPI()
templates = Jinja2Templates(directory="./lesson/templates")


@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("index.html", {"request": request, "name": name})