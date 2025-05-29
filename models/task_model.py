from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    description: str
    id_user: int
    id_type_task: int
    id_tag_task: int
    repeat_interval: Optional[str] = None