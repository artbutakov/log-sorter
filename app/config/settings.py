from dotenv import load_dotenv
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


load_dotenv()


class DatabaseSettings(BaseSettings):
    name: str = Field(validation_alias='DATABASE_NAME')
    username: str = Field(validation_alias='DATABASE_USER')
    password: SecretStr = Field(validation_alias='DATABASE_PASSWORD')


database_settings = DatabaseSettings()
