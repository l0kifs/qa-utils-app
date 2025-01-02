from typing import Optional

from pydantic import BaseModel


class CreateAutomationTaskRequest(BaseModel):
    email: str
    password: str
    task_type: str
    task_name: str
    task_description: str
    test_suite: str
    test_key: str
