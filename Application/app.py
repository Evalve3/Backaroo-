from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from Application.views.collect.collect import collect_router
from Application.views.file.file import file_router
from Application.views.user.user import user_router


def create_app() -> FastAPI:
    app = FastAPI(openapi_url="/Application/openapi.json", docs_url="/core/docs")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )

    app.include_router(user_router)
    app.include_router(file_router)
    app.include_router(collect_router)

    return app
