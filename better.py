from pydantic import BaseSettings

# from dotenv import load_dotenv
# load_dotenv()

class Settings(BaseSettings):
    mysql_user: str = "Awesome API"
    mysql_password: str = "wuffig"
    mysql_database: int = 50


settings = Settings().dict()
print(settings)