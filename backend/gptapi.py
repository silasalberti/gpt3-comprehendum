from typing import List

import requests
from dotenv import load_dotenv
import os
import openai

load_dotenv()

API_KEY = os.getenv("APIKEY")
# openai.apikey = API_KEY

# openai.Answer.create()

answers_url = "https://api.openai.com/v1/answers"
header_auth = f"Bearer {API_KEY}"
header_contenttype = "application/json"

search_model = "ada"
completion_model = "curie"

examples_context = """6.6.1.3	Decent Working Time

Violations of working time through the practices of state and non-state actors my limit the right of a person to 
decent working hours. Siemens may face several operational, financial, legal and reputational risks where these 
standards aren't met. Specific risks may arise from potential violations of working hours regulations 
project business on the part of suppliers, subcontractors or other businesses involved in the project.
Definition of the Issue
The right to decent working time is enshrined in Article 7 of the International Covenant on Economic, Social and 
Cultural Rights (ICESCR). Specifically, workers are entitled to the right to rest, leisure, reasonable limitation 
of working hours and adequate holiday allowances with pay. These conditions are linked to basic human 
rights including the right to an adequate standard of living (including adequate food, clothing and housing), the 
right to physical and mental health and the right to life.
Numerous ILO conventions provide for more detailed provisions on decent working hours laid down in the 
ICESCR. ILO convention 1 stipulates that generally working time should not exceed 48 hours per week, or 
eight hours a day, with at least one day off in every seven. ILO convention 30 states a working day cannot 
exceed ten hours. Furthermore, ILO convention 1 also states that where overtime work is allowed and required, 
the maximum number of additional hours must be fixed, and overtime must be compensated at a rate of 
no less than 25% above the normal rate of pay.
"""
examples = [
    [
        "Where is the right to decent working hours defined?",
        "In Article 7 of the International Covenant on Economic, Social and Cultural Rights (ICESCR)."
    ],
    [
        "How should overtime be compensated?",
        "At least 25% above the normal rate of pay."
    ],
    [
        "What risks does Siemens face when the decent working hour standards are not met?",
        "Siemens risks being faced with operational, financial, legal and reputational risks."
    ],
]


def get_answer(question: str, paragraphs: List[str]):
    # question = "Is a payment under duress deemed an act of corruption?"

    response = requests.post(
        answers_url,
        headers={
            "Authorization": header_auth,
            "Content-Type": header_contenttype
        },
        json={
            "documents": paragraphs,
            "question": question,
            "search_model": search_model,
            "model": completion_model,
            "examples_context": examples_context,
            "examples": examples,
            "max_tokens": 200,
            "stop": ["\n", "<|endoftext|>"],
            "temperature": 0
        }
    )
    return response.json()['answers'][0]
