from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import main

app = FastAPI(
    title=settings.PROJECT_NAME
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/docs", include_in_schema=False)
async def swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui.css"
    )


app.include_router(main.api_router)
