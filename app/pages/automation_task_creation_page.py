from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/automation_task_creation", response_class=HTMLResponse)
async def automation_task_creation_page(request: Request):
    return templates.TemplateResponse("automation_task_creation_template.html", {"request": request})
