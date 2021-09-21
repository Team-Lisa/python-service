from pydantic.main import BaseModel


class User(BaseModel):
    name: str
