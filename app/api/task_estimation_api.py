from fastapi import APIRouter, HTTPException

from app.core.task_estimation_logic import calculate_complexity, estimate_time
from app.models.task_estimation_models import EstimateTaskRequest

router = APIRouter(prefix="/api")


@router.post("/estimate_task")
async def estimate_task(request_body: EstimateTaskRequest):
    try:
        complexity = calculate_complexity(
            criteria_scores=[value for _, value in request_body.criteria.model_dump().items()],
            overall_risk=request_body.risk_level, 
            risk_multiplier=0.2
        )
        estimated_time = estimate_time(min_time=2, max_time=40, complexity=complexity)
        return {"complexity": round(complexity, 2), "estimated_time": estimated_time}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
