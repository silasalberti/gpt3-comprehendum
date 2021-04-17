from fastapi import Request
from index import app, ask_question
from pydantic import BaseModel
import requests

import logging
from slackers.hooks import commands

log = logging.getLogger(__name__)

@commands.on("comprehendum")
def handle_mention(payload):
    print(payload["channel_id"])

    channel_id = payload["channel_id"]

    if channel_id == "C01UFQDJ22H":
        question = payload["text"]
        result = ask_question(question)

        requests.post(payload["response_url"], json= {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Question:* {question}" 
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Answer:* {result}" 
                    }
                }
            ]
        })
    else:
        requests.post(payload["response_url"], json= {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Not allowed in this channel" 
                    }
                },
            ]
        })



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
                        "text": f"Answer:* {ask_question(question)}"
                    }
                }
            ]
        }
    else:
        return f"You can't use this bot from the {channel_name} channel!!! :=("

