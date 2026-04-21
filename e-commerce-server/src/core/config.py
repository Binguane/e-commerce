from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f'{BASE_DIR}/.env'
    )
    app_name: str = 'MozOnWheels'
    DATABASE_URL_DEV: SecretStr
    ALGORITHM:str
    SECRET_KEY:SecretStr

settings = Settings()
