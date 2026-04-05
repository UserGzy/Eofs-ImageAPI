from fastapi import FastAPI,Response,Request
from fastapi.responses import FileResponse
from pyexiv2 import Image as exiv_img
import os
import random,time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

MAX_THREADS = 16

app = FastAPI()

img_list = {}

tag_lock = Lock()
tag_list = {}
tag_str = ""

def GetDeviceType(UA=""):
    if "mobile" in UA:
        return "phone"
    else:
        return "PC"
    
def GenTagList():
    global img_list
    global tag_str
    with ThreadPoolExecutor(max_workers = MAX_THREADS) as executor:
        executor.map(GenTagListOne,img_list)
    tag_list["default"] = img_list
    tag_str = tag_str + "default"
    print("[info] Tag List generate completed.")
    #print(tag_list)

def GenTagListOne(img_name):
    global tag_list
    global tag_str
    img_path = "./imgs/" + img_name
    img = exiv_img(img_path)
    metadata = img.read_xmp()
    for tag in metadata.get('Xmp.dc.subject', []):
        with tag_lock:
            if not (tag in tag_list):
                tag_list[tag]=[img_name]
                tag_str = tag_str + tag + ", "
            else:
                tag_list[tag].append(img_name)
    img.close()

@app.on_event("startup")
def initial():
    print("[info] App starting")

    random.seed(time.time())

    print("[info] Loading file list")
    global img_list
    img_list = os.listdir("./imgs/")

    print(f"[info] Loaded {len(img_list)} images from folder")

    GenTagList()

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

@app.get("/loading.png")
def LoadingPic():
    return FileResponse("./loading.png")

@app.get("/api/random")
def returnRandomPic(q: str = "default"):
    global tag_list
    img_name = random.choice(tag_list.get(q,["none.png"]))
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

@app.get("/api/tagstr")
def returnTagstr():
    global tag_str
    return tag_str


@app.get("/css/{name}")
def returnCSS(name:str):
    return FileResponse("./css/"+name)