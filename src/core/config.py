from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    SLACK_TOKEN: str
    GITHUB_TOKEN: str


@lru_cache
def get_settings():
    return Settings()
