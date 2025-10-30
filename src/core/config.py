from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "sql_report"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    @property
    def DATABASE_URL(self):
        return (
            f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

settings = Settings()
