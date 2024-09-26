from typing import Optional
from returns.maybe import Maybe
from config.base import session_factory
from models import Type


def find_type_by_id(type_id: int) -> Optional[Type]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Type)
            .filter(Type.target_type_id == type_id)
            .first()
        )
