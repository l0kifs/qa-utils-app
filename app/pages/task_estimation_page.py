from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/task_estimation", response_class=HTMLResponse)
async def task_estimation_page(request: Request):
    return templates.TemplateResponse("task_estimation_template.html", {"request": request})
