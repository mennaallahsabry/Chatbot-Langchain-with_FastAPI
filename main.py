# fastapi_app/main.py
from fastapi import FastAPI
from fastapi_app.app_router import router as app_router

app = FastAPI()

app.include_router(app_router)
#, prefix="/query", tags=["query"]