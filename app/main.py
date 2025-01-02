from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import automation_task_creation_api, task_estimation_api
from app.pages import automation_task_creation_page, task_estimation_page, home_page


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home_page.router)
app.include_router(task_estimation_api.router)
app.include_router(task_estimation_page.router)
app.include_router(automation_task_creation_api.router)
app.include_router(automation_task_creation_page.router)
