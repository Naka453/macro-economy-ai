from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_gpt(question: str) -> str:
    response = client.responses.create(
        model="gpt-6-astra",
        reasoning={
            "effort": "high"
        },
        input=question
    )

    return response.output_text