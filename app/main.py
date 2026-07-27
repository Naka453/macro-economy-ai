from fastapi import FastAPI

from app.api.chat import router

app = FastAPI(
    title="Macro Economy AI Agent",
    version="1.0"
)

app.include_router(router)