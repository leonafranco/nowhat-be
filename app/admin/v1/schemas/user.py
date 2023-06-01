from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.admin.models.user import User
from marshmallow import Schema, fields


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User


class PostUserSchema(UserSchema):
    class Meta(UserSchema.Meta):
        exclude = ("id",)


class UsersSchema(UserSchema):
    items = fields.List(fields.Nested(UserSchema))
