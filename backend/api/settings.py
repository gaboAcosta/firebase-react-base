from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql://postgres:example@127.0.0.1/postgres'
