# fastapi_app/query_router.py
from fastapi import APIRouter
from langchain_app.langchain_utils import LangchainUtils, Message

router = APIRouter()
langchain_utils = LangchainUtils()

@router.get("/")
async def ping():
    print("ping")
    return {"message": "Hello World"}

@router.get("/ping")
async def pong():
    print("ping")
    return "pong!"

@router.post("/ask/")
async def run_query(input_data: Message):
    print("yes")
    #query = input_data.content
    # result = langchain_utils.run_query(query)
    #return {"response": result}
    return {"response": "Success"}


