from pydantic import BaseModel


class TaskCriteria(BaseModel):
    effort: int
    clarity: int
    risks: int
    experience: int
    communication: int

class EstimateTaskRequest(BaseModel):
    criteria: TaskCriteria
    risk_level: int
