from fastapi import APIRouter

from common.language_model import LanguageModel
from endpoints.models.chat_request import ChatRequest


def get_chat_router(settings):
    router = APIRouter()

    @router.post("/chat")
    async def chat(request: ChatRequest):
        if request.profile_name not in settings.profiles:
            return {"error": "Profile not found"}

        profile = settings.profiles[request.profile_name]
        session = settings.get_session(request.session_name)

        history = settings.get_history(request.session_name, profile['max_history'])

        config = profile['config']
        llm = LanguageModel(config)
        response = llm.ask(request.question, history)

        # セッションにメッセージを追加
        session.add_message("user", request.question)
        session.add_message("assistant", response[0])

        return response

    return router
