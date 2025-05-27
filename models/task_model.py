from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    description: str
    type: str = "Simple"
    id_user: int = 1
    id_type_task: int = 1
    id_tag_task: int = 1
    repeat_interval: Optional[str] = None