from fastapi import FastAPI, Form, File, UploadFile
import aiofiles
from typing import Optional

app = FastAPI()


@app.post("/form")
def basic_form(username: str = Form(...), password: str = Form(default=..., min_length=8)):
    print(username, password)
    return { "username": username }



# @app.post("/fileform")
# def file_form(file: bytes = File(...), description: Optional[str] = Form(None)):
#     with open('file', 'wb') as f:
#         f.write(file)

#     return { "message": "File Uploaded" }


# @app.post("/fileform")
# async def file_form(file: UploadFile = File(...), description: Optional[str] = Form(None)):
#     contents = await file.read()
#     print(contents)

#     return { "filename": file.filename }



# @app.post("/fileform")
# async def file_form(file: UploadFile = File(...), description: Optional[str] = Form(None)):
#     safe_filename = file.filename.replace("/", "_").replace("\\", "_")

#     with open (safe_filename, 'wb') as f:
#               # walrus operator
#         while content := await file.read(1024): # read in 1024 chunks
#             f.write(content)


@app.post("/fileform")
async def file_form(file: UploadFile = File(...), description: Optional[str] = Form(None)):
    print(description)

    safe_filename = file.filename.replace("/", "_").replace("\\", "_")

    # aiofiles ensures that it's asynchronous
    async with aiofiles.open (safe_filename, 'wb') as f:
              # walrus operator
        while content := await file.read(1024): # read in 1024 chunks
            await f.write(content)