from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="src")

app.mount("/public", StaticFiles(directory="public"), name="public")
app.mount("/node_modules", StaticFiles(directory="node_modules"), name="node_modules")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(name="pages/index.html", context={"request": request}, status_code=200)