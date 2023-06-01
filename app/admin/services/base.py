from typing import Final, Generic, Optional, Type

from app.stores.database import db
from app.types.models import ModelInstance


class Base(Generic[ModelInstance]):
    _model: Type[ModelInstance]

    def get_by_id(self, id) -> Optional[ModelInstance]:
        record = db.session.get(self._model, id)

        return record

    def get_all(self) -> Optional[ModelInstance]:
        return db.session.query(self._model).all()

    def create(self, **data) -> Optional[ModelInstance]:
        try:
            record: Final = self._model(**data)
            db.session.add(record)
            db.session.commit()

            return record
        except Exception:
            db.session.rollback()
            raise
