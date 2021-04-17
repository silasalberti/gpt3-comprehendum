from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from time import sleep

from gptapi import get_answer
from key_word_search import get_sentences

# set permitted cors origins
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
    # TODO: populate database/preprocess text files
    print("app started")


@app.on_event("shutdown")
async def shutdown():
    print("app stopped")


# see here: https://fastapi.tiangolo.com/advanced/response-directly/

test_paragraphs = [
    "All Siemens employees are prohibited from offering, promising or making facilitation payments . No such authorization will be granted. The same applies to payments or the granting of other benefits of comparable characteristics and with a comparable purpose to private commercial counterparties.",
    "This prohibition may not be circumvented by making facilitation payments indirectly through third parties . When working with third parties, employees must therefore look out for any indications, for example on invoices, that such third parties may have made or may be making facilitation payments in the context of their activities for Siemens.",
    "In many jurisdictions, a payment under duress is not deemed an act of corruption. In other countries, a situation of duress is at least recognized as justification or as grounds for exemption from punishment. Correspondingly, no Siemens employees are expected to risk life, limb or liberty in the course of performing their duties. Unjustified payments under duress will therefore not be punished with disciplinary action under the following conditions: Any employee should ask the person demanding the payment to explain the legal basis for the demand and inquire whether an official account or receipt will be issued for the payment . If it becomes evident that the payment demanded most likely constitutes a facilitation payment, either because there is no plausible legal basis for such payment or because the government official refuses to issue an official invoice or receipt, the employee should oppose the demand as strongly as possible. If a situation of duress arises, it is permissible to yield to the request to make a facilitation payment. Expenditure in connection with facilitation payments is generally not reimbursed to employees or third parties acting for Siemens . Provided that the employee has complied in full with the applicable reporting and documentation obligations and there are no specific circumstances indicating that the employee is at fault in connection with the payment, disciplinary action will generally be disproportionate because the employee will have allowed Siemens to meet its statutory documentation duties."]


@app.get("/api/question")
async def question(q: str):
    # request_body = await request.json()
    print(q)
    # TODO: Get keywords from request_body.query (The question) using stop words dict
    # TODO: Look for relevant paragraphs in paragraphs array
    # TODO: Send request with appropriate token size (10000?) to gpt-3 to get an answer
    paragraphs = get_sentences(q)
    answer = get_answer(q, paragraphs)
    # TODO: return answer
    print(answer)
    result = jsonable_encoder({"answer": answer})

    # dummy wait to test frontend animations
    # sleep(2)
    return JSONResponse(content=result)
