from functools import cached_property

from flask import abort
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
import openai
from app.admin.services.openai import OpenAIService
from app.admin.v1.schemas.openai import OpenAISchema


@doc(description="OpenAi API", tags=["admin/openai"])
class OpenAiResource(MethodResource):
    @cached_property
    def service(self):
        return OpenAIService()

    @marshal_with(OpenAISchema)
    def get(self):
        models = openai.Model.list()
        print(models.data[0].id)
        print("Space")
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
        print(chat_completion)
        print("space")
        return (chat_completion.choices[0].message.content)
