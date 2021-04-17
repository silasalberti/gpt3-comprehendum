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
            "examples_context": "A facilitation payment is the payment of a relatively small amount of money or the granting of any other benefit to usually low-ranking government officials, for their own personal benefit, with the aim of speeding up the performance of an official act to which the person making the payment/granting the benefit is entitled. This means that the government entity concerned would perform the official act in the same form and in any event, without payment to the government official (including, for example, granting approval where all preconditions are satisfied).",
            "examples": [["Who does a facilitation payment go to?", "Low-ranking government officials."]],
            "max_tokens": 40,
            "stop": ["\n", "<|endoftext|>"],
            "temperature": 0.2
        }
    )
    return response.json()['answers'][0]
