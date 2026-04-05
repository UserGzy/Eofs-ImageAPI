# Eofs-ImageAPI
## Introduction · 简介
一个基于Python的轻量级随机图片API<br>
支持按图片标签（Xmp.dc.subject）筛选图片<br>
<br>
A lightweight random image API based on Python.<br>
Supports filtering images by image tag (Xmp.dc.subject).<br>
<br>
## Usage · 使用方法<p></p>
***Create Environment · 创建环境***<br>
`python -m venv .venv`<br>
<br>
***Install dependencies in the env · 在环境内安装依赖***<br>
`(.venv) pip install -r requirements.txt`<br>
<br>
***Start up · 启动***<br>
`(.venv) uvicorn main:app --port <your port> --host 0.0.0.0`<br>
<br>
然后访问设定的端口即可<br>
Then access the webpage from your port.<br>
<br>
## Extra · 额外内容<p></p>
使用如下命令安装***Tailwind CSS***以继续开发网页。
<br>Use following commands install ***TailWind CSS*** to continue developing webpage.<br>
<br>

    npm install
    npx @tailwindcss/cli -i ./style.css -o ./css/outputs.css --watch
