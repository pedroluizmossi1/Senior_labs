import fastapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from endpoints import api

api.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@api.get("/test", response_class=HTMLResponse)
async def root():
    return templates.TemplateResponse("index.html")

