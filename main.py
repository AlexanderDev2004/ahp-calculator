from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from livereload import Server
from threading import Thread

app = FastAPI()
templates = Jinja2Templates(directory="src")

def start():
    server = Server()
    server.watch("public/**/*")
    server.watch("src/**/*")
    server.watch("main.py")
    server.serve(host="127.0.0.1", port=35729)

Thread(target=start, daemon=True).start()

app.mount("/public", StaticFiles(directory="public"), name="public")
app.mount("/node_modules", StaticFiles(directory="node_modules"), name="node_modules")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(name="pages/index.html", context={"request": request}, status_code=200)

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(name="pages/about.html", context={"request": request}, status_code=200)

@app.get("/ahp")
def about(request: Request):
    return templates.TemplateResponse(name="pages/ahp.html", context={"request": request}, status_code=200)

@app.get("/calculate")
def about(request: Request):
    return templates.TemplateResponse(name="pages/calculate.html", context={"request": request}, status_code=200)

@app.get("/help")
def help(request: Request):
    return templates.TemplateResponse(name="pages/help.html", context={"request": request}, status_code=200)