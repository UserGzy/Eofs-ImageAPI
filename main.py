from fastapi import FastAPI,Response,Request
from fastapi.responses import FileResponse
import os
import random,time

app = FastAPI()

img_list = {}

def GetDeviceType(UA=""):
    if "mobile" in UA:
        return "phone"
    else:
        return "PC"

@app.on_event("startup")
def initial():
    print("[info] App starting")

    random.seed(time.time())

    print("[info] Loading file list")
    global img_list
    img_list = os.listdir("./imgs/")

    print(f"[info] Loaded {len(img_list)} images from folder")

@app.get("/")
def HomePage(request:Request):
    ua = request.headers.get('User-Agent').lower()
    if GetDeviceType(ua) == "phone":
        print("[info] Send main_H")
        return FileResponse("./main_H.html")
    else:
        print("[info] Send main_W")
        return FileResponse("./main_W.html")

@app.get("/favicon.ico")
def HomePage():
    return FileResponse("./favicon.ico")

@app.get("/api/random")
def returnRandomPic(q: str = None):
    global img_list
    img_name = random.choice(img_list)
    print("[info] Send image '"+img_name+"'")
    response = FileResponse(os.path.join("./imgs/", img_name))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.get("/api/totalnum")
def returnPicNum():
    global img_list
    return len(img_list)

@app.get("/css/{name}")
def returnCSS(name:str):
    return FileResponse("./css/"+name)