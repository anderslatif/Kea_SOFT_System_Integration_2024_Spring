from fastapi import FastAPI, Form, File


app = FastAPI()


@app.post("/form")
def basic_form(username: str = Form(...), password: str = Form(default=..., min_length=8)):
    print(username, password)
    return { "username": username }



@app.post("/fileform")
def file_form(file: bytes = File(...)):
    with open('file', 'wb') as f:
        f.write(file)

    return { "message": "File Uploaded" }

