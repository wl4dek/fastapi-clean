from dependency_injector import containers, providers

from src.config.database import Database
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Singleton(Database, db_url=config.db_url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
