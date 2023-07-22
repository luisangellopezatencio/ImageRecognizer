from fastapi import FastAPI, File, UploadFile, Request
from typing import Optional
import utils
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates  = Jinja2Templates(directory = "templates")

#cargar el html
@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

#Cuando se le da al boton enviar llama a esta solicitud post
@app.post("/")
async def home_predict(request:Request, file:UploadFile = File(...)):
    result = utils.get_result(image_file = file)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

@app.post("/predict")
async def predict(file:UploadFile = File(...)):
    return utils.get_result(image_file = file)

