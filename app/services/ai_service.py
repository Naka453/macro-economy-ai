from pathlib import Path

from openai import OpenAI

from app.config import OPENAI_API_KEY, VECTOR_STORE_ID

client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT = Path("app/prompts/system_prompt.txt").read_text(
    encoding="utf-8"
)


def ask(question: str):

    response = client.responses.create(

        model="gpt-6-astra",

        reasoning={
            "effort": "high"
        },

        instructions=PROMPT,

        input=question,

        tools=[
            {
                "type": "file_search",
                "vector_store_ids": [VECTOR_STORE_ID]
            }
        ]
    )

    return response.output_text