from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="タスク")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int

    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True