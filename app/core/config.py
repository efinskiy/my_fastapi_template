import os
from functools import lru_cache
from typing import Literal, Annotated, Any, ClassVar

from pydantic import PostgresDsn, BeforeValidator, AnyUrl, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    _APP_ENV = os.environ['APP_ENV']
    match _APP_ENV:
        case 'prod':
            _ENV_FILE = '.env.prod'
        case 'dev':
            _ENV_FILE = '.env.dev'

        case _:
            _ENV_FILE = '.env.dev'

    model_config = SettingsConfigDict(
        env_file=_ENV_FILE, env_ignore_empty=True, extra='ignore'
    )

    SECRET_KEY: str = 'test'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = 'localhost'
    ENV: Literal['dev', 'prod'] = 'dev'

    PROJECT_NAME: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
