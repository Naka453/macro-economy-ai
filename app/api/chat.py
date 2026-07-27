from fastapi import APIRouter

from app.models.request import ChatRequest
from app.models.response import ChatResponse

from app.services.ai_service import ask

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    answer = ask(request.question)

    return ChatResponse(answer=answer)