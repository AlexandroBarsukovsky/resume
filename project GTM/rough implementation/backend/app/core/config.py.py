from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://sg_user:sg_pass@postgres:5432/sg_gtm_db"
    DB_NAME: str = "sg_gtm_db"
    DB_USER: str = "sg_user"
    DB_PASSWORD: str = "sg_pass"

    # Redis
    REDIS_URL: str = "redis://:redis_pass@redis:6379"
    REDIS_PASSWORD: str = "redis_pass"

    # Salesforce
    SF_USERNAME: Optional[str] = None
    SF_PASSWORD: Optional[str] = None
    SF_TOKEN: Optional[str] = None

    # Gainsight
    GAINSIGHT_API_KEY: Optional[str] = None

    # 6sense
    SIXSENSE_API_KEY: Optional[str] = None

    # SalesLoft
    SALESLOFT_API_KEY: Optional[str] = None

    # Hightouch
    HIGHTOUCH_API_KEY: Optional[str] = None

    # Snowflake
    SNOWFLAKE_ACCOUNT: Optional[str] = None
    SNOWFLAKE_USER: Optional[str] = None
    SNOWFLAKE_PASSWORD: Optional[str] = None

    # Security
    SECRET_KEY: str = "change_this_in_production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()