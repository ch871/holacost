from typing import Optional
from returns.maybe import Maybe
from config.base import session_factory
from models import City


def find_city_by_id(city_id: int) -> Optional[City]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(City)
            .filter(City.city_id == city_id)
            .first()
        )

