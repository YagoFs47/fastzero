from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR.joinpath('.env'), 
        env_file_encoding='utf-8'
    )

    DATABASE_URL: str
