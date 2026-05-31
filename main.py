from fastapi import FastAPI, Body, Request
from gemini_client import ask_gemini
from datetime import datetime
from contextlib import asynccontextmanager
from db import Base,engine
from db import ChatRequests
from db import get_user_requests,add_request_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    print("Created DB")
    yield


app = FastAPI(
    title="Gemini API",
    lifespan=lifespan
    )

@app.post("/")
def send_prompt(
    request:Request,
    prompt: str=Body(embed=True)
    ):
    answer = ask_gemini(prompt)
    add_request_data(ip_address=request.client.host,prompt=prompt,response=answer)
    return {"answer": answer }

@app.get("/requests")
def get_requests(request:Request):
    user_ip_address=request.client.host
    print(user_ip_address)
    user_requests=get_user_requests(ip_address=user_ip_address)
    return user_requests

@app.get("my_requests/{request_id}")
def get_request(request:Request,request_id:int):
    user_ip_address=request.client.host
    user_request=get_user_requests(ip_address=user_ip_address)[request_id]
    return user_request



