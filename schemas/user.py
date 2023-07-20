from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    job: str