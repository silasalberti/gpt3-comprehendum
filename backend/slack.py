from index import app

@app.post("/api/questionBySlack")
def question_by_slack(request: Request):
    print(request.json())
