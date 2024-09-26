from typing import Optional

from returns.maybe import Maybe, Nothing
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from models import Target
from returns.result import Result, Success, Failure


def insert_target(target: Target):
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def get_all_targets():
    with session_factory() as session:
        return session.query(Target).all()


def find_target_by_id(target_id: int) -> Optional[Target]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Target)
            .filter(Target.target_id == target_id)
            .first()
        )


def delete_target(target_id: int):
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure("no target with thees id ")
            target_to_delete = session.merge(maybe_target.unwrap())
            session.delete(target_to_delete)
            session.commit()
            return Success(target_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def update_target(target_id: int, target: Target):
    with session_factory() as session:
        try:
            maybe_target = find_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure("no target with thees id ")
            target_to_update = session.merge(maybe_target.unwrap())
            target_to_update.target_industry = target.target_industry
            target_to_update.target_priority = target.target_priority
            target_to_update.target_type_id = target.target_type_id
            target_to_update.city_id = target.city_id

            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))
