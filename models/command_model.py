from pydantic import BaseModel
from typing import Optional



class CommandLog(BaseModel):
    phrase: str
    action: Optional[str]
    type: Optional[str]