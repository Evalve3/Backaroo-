from fastapi import FastAPI

from Application.views.file.file import file_router
from Application.views.user.user import user_router


def create_app() -> FastAPI:
    app = FastAPI(openapi_url="/Application/openapi.json", docs_url="/core/docs")

    app.include_router(user_router)
    app.include_router(file_router)

    return app
