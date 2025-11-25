from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: List[str] = []

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def split_allowed_origins(cls, v: str | List[str]) -> List[str]:
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings() # type: ignore