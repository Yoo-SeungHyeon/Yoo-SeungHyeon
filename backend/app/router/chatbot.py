from fastapi import APIRouter

chat_router = APIRouter(prefix="/chat", tags=["chatbot"])

@chat_router.post("/ask")
async def ask_chatbot(question: str):
    """
    Chatbot에 질문을 보내면 답변을 리턴합니다.
    """
    # TODO: 실제 챗봇 응답 로직 구현
    return {"answer": f"'{question}'에 대한 답변입니다."}