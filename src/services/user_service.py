from src.schema.user import UserIn
from typing import Iterator
from src.repositories.user_repository import UserRepository
from src.models.user import User


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self, user_in: UserIn) -> User:
        return self._repository.add(email=user_in.email, password=user_in.hashed_password)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
