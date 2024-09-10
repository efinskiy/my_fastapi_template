from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html

from app.api.routes import test
from app.core.config import settings

api_router = APIRouter()


if settings.ENV == 'dev':
    api_router.include_router(test.router, prefix='/dev', tags=['Dev features'])

