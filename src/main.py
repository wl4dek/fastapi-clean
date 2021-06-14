from fastapi import FastAPI
from src.containers import Container
from src.routes import user
from src.config.settings import DB_URL, V1


def create_app() -> FastAPI:
    container = Container()
    container.config.from_dict({'db_url': DB_URL})
    container.wire(modules=[user])

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(user.router, prefix=V1)
    return app


app = create_app()
