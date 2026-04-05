# Eofs-ImageAPI
## Introduction · 简介
一个基于Python的轻量级随机图片API<br>
具有如下特性：  
- 支持按图片标签（Xmp.dc.subject）筛选图片
- 自动读取标签并建立索引，导入图片后可以直接通过参数查询
- 支持根据User-Agent判断设备类型并返回特定的图片（横板/竖版）
  
A lightweight random image API based on Python.  
It has the following features:  
- Supports filtering images by image tag (Xmp.dc.subject)
- Automatically reads tags and builds an index; images can be directly queried by parameters after importing them
- Supports determining the device type based on the User-Agent and returning specific images (landscape/portrait)
   
## Usage · 使用方法  
***Create Environment · 创建环境***<br>
`python -m venv .venv`  
  
***Install dependencies in the env · 在环境内安装依赖***<br>
`(.venv) pip install -r requirements.txt`  
  
***Start up · 启动***  
`(.venv) uvicorn main:app --port <your port> --host 0.0.0.0`  
  
然后访问设定的端口即可  
Then access the webpage from your port.<br>
<br>
## Extra · 额外内容  
使用如下命令安装***Tailwind CSS***以继续开发网页。
  Use following commands install ***TailWind CSS*** to continue developing webpage.  
  

    npm install
    npx @tailwindcss/cli -i ./style.css -o ./css/outputs.css --watch
