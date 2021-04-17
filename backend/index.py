from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from time import sleep
#set permitted cors origins
origins = [
    "*"
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

@app.get("/api/question")
async def question(question: str):
    # request_body = await request.json()
    print(question)
    # TODO: Get keywords from request_body.query (The question) using stop words dict
    # TODO: Look for relevant paragraphs in paragraphs array
    # TODO: Send request with appropriate token size (10000?) to gpt-3 to get an answer
    # TODO: return answer
    result = jsonable_encoder({"answer": "a"*2000})
    
    #dummy wait to test frontend animations
    sleep(2)
    return JSONResponse(content=result)