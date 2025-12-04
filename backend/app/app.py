from fastapi import FastAPI
from app.schema.utils import HealthCheckResponse
from app.router.chatbot import chat_router

app = FastAPI()

@app.get(
    "/", 
    summary="Health Check",
    response_model=HealthCheckResponse,
    response_model_exclude_unset=True
)
async def root():
    """
    Health check endpoint.
    """
    return HealthCheckResponse(status=200)

app.include_router(chat_router)
