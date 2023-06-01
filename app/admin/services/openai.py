from app.admin.models.openAI import OpenAI
from app.admin.services.base import Base


class OpenAIService(Base[OpenAI]):
    def __init__(self):
        self._model = OpenAI
