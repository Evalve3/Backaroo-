from fastapi import FastAPI

from Application.views.user.user import user_router


def create_app() -> FastAPI:
    app = FastAPI(openapi_url="/Application/openapi.json", docs_url="/core/docs")

    app.include_router(user_router)

    return app
