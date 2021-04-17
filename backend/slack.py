from fastapi import Request
from index import app
from pydantic import BaseModel

class SlackQuestion(BaseModel):
    # token: str
    # team_id: str
    # team_domain: str
    # enterprise_id: str
    # enterprise_name: str
    # channel_id: str
    # channel_name: str
    # user_id: str
    # user_name: str
    command: str
    text: str
    # response_url: str
    # trigger_id: str
    # api_app_id: str

@app.post("/api/questionFromSlack")
async def question_by_slack(request: Request):
    body = await request.form()
    print(body)
    channel_name = body["channel_name"]
    question = body["text"]
    if channel_name == "smashers":
        return {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Your Question:* {question}"
                    }
                }
            ]
        }
    else:
        return f"You can't use this bot from the {channel_name} channel!!! :=("

