from fastapi import APIRouter, HTTPException
import requests

from app.models.automation_task_creation_models import CreateAutomationTaskRequest
from app.core.automation_task_creation_logic import create_task

router = APIRouter(prefix="/api")


@router.post("/create_automation_task")
async def create_automation_task(request_body: CreateAutomationTaskRequest):
    try:
        result = create_task(request_body)
        return {'detail': result}
    except (ValueError, requests.exceptions.HTTPError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
