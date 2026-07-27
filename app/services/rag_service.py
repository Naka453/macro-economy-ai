from openai import OpenAI
from app.config import OPENAI_API_KEY, VECTOR_STORE_ID

client = OpenAI(api_key=OPENAI_API_KEY)


def ask(question: str):

    response = client.responses.create(
        model="gpt-5.5",
        input=question,
        tools=[
            {
                "type": "file_search",
                "vector_store_ids": [VECTOR_STORE_ID]
            }
        ]
    )

    return response.output_text