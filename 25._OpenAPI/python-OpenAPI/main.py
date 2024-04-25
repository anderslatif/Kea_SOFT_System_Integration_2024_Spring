from fastapi import FastAPI

app = FastAPI()

from routers import spacecraft_router
app.include_router(spacecraft_router)


import json
# Commented out since this runs on startup and would run too often with the uvicorn --reload flag
# @app.on_event("startup")
# def save_openapi_json():
#     openapi_data = app.openapi()
#     # Change "openapi.json" to desired filename
#     with open("openapi.json", "w") as file:
#         json.dump(openapi_data, file)