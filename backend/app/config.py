from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:password@localhost:5432/vitasage_271527"
    jwt_secret: str = "change-me-in-production-please-use-env-var"
    jwt_algorithm: str = "HS256"
    jwt_expire_hours: int = 8
    allowed_origins: str = "*"   # Override via ALLOWED_ORIGINS env var in prod
    register_secret: str = "vitasage-bootstrap-secret"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
