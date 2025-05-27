from pydantic import BaseModel

class CommandLog(BaseModel):
    phrase: str
    action: str = None
    type: str = None