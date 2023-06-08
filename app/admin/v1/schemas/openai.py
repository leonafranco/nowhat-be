from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.admin.models.user import User
from marshmallow import Schema, fields


class OpenAISchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User


class PostOpenAISchema(OpenAISchema):
    class Meta(OpenAISchema.Meta):
        exclude = ("id",)


class OpenAisSchema(OpenAISchema):
    items = fields.List(fields.Nested(OpenAISchema))
