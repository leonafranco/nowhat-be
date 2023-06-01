from app.admin.models.user import User
from app.admin.services.base import Base


class UserService(Base[User]):
    def __init__(self):
        self._model = User
