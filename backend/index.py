from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from time import sleep
#set permitted cors origins
origins = [
    "http://localhost:3000"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    #TODO: populate database/preprocess text files
    print("app started")


@app.on_event("shutdown")
async def shutdown():
    print("app stopped")


# see here: https://fastapi.tiangolo.com/advanced/response-directly/

@app.post("/api/question")
async def question(request: Request):
    #TODO: prepare and make gpt-3 query here
    request_body = await request.json()
    #TODO: deal with request_body.query (The question)
    result = jsonable_encoder({"answer": "a"*2000})
    
    #dummy wait to test frontend animations
    sleep(2)
    return JSONResponse(content=result)