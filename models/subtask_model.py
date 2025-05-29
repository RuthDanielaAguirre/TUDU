from pydantic import BaseModel
from typing import Optional
from datetime import date

class SubtaskCreate(BaseModel):
    description: str
    id_task_parent: int
    state: int
    due_date: Optional[date]
