from fastapi import Request
from index import app, ask_question
from pydantic import BaseModel
import random
import requests
from multi_rake import Rake
rake = Rake()

import logging
from slackers.hooks import commands

log = logging.getLogger(__name__)

users = [
    {
        "id": "U01T7Q8NE3U",
        "name": "Silas Alberti",
        "pronoun": "He"
    },
    {
        "id": "U01T468DJ6R",
        "name": "Marc Schneider",
        "pronoun": "He"
    },
    {
        "id": "U01T7AR57V0",
        "name": "Simon Bohnen",
        "pronoun": "He"
    },
    {
        "id": "U01TZA1M800",
        "name": "Ria Rosenauer",
        "pronoun": "She"
    },
    {
        "id": "U01T4ASN329",
        "name": "Alexander von Recum",
        "pronoun": "He"
    }
]

@commands.on("comprehendum")
def handle_mention(payload):
    # requests.post(payload["response_url"], json={
    #     "blocks": [
    #         {
    #             "type": "section",
    #             "text": {
    #                 "type": "mrkdwn",
    #                 "text": f"_Processing..._" 
    #             }
    #         },
    #     ]
    # })

    print(payload["channel_id"])

    channel_id = payload["channel_id"]

    if channel_id == "C01UFQDJ22H":
        question = payload["text"]
        result = ask_question(question)

        l = rake.apply(question)
        keyword = max(l, key=lambda _:_[0])[0] if l is not None and len(l) > 0 else "legal & compliance"
        random.seed(hash(keyword))
        user = random.choice(users)
        nl = "\n"

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
                        "text": f"> *Answer:* Hey <@{payload['user_id']}>! "
                        f"{result.split(nl)[0]}{nl}{nl.join(['> ' + line for line in result.split(nl)[1:]])}" 
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"_For specific support contact <@{user['id']}> from the "
                                f"legal & compliance "
                                f"department. {user['pronoun']} is the correct contact "
                                f"person for issues concerning *\"{keyword}\"*. 😀_"
                    }
                },
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

