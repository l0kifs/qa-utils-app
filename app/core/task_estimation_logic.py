def calculate_complexity(
        criteria_scores: list[int],
        overall_risk: int,
        risk_multiplier: float
    ) -> float:
    if not all(1 <= score <= 5 for score in criteria_scores):
        raise ValueError("All criteria scores must be between 1 and 5.")
    if not (1 <= overall_risk <= 5):
        raise ValueError("Overall risk level must be between 1 and 5.")
    if not (0 <= risk_multiplier <= 1):
        raise ValueError("Risk multiplier must be between 0 and 1.")
    
    average_complexity =  sum(criteria_scores) / len(criteria_scores)
    adjusted_complexity = min(max(average_complexity * (1 + (overall_risk - 1) * risk_multiplier), 1), 5)
    return adjusted_complexity


def estimate_time(
        min_time: float,
        max_time: float,
        complexity: float
    ) -> float:    
    estimated_time = min_time + (complexity - 1) * (max_time - min_time) / (5 - 1)
    return round(estimated_time)
