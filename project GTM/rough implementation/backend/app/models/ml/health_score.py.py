# backend/app/models/ml/health_score.py

def compute_health_score(deficit_norm: float, turnover_norm: float, margin_norm: float) -> float:
    """Health Score = 0.4*deficit + 0.3*turnover + 0.3*marginality"""
    return 0.4 * deficit_norm + 0.3 * turnover_norm + 0.3 * margin_norm

def classify_health_score(health: float) -> str:
    if health >= 0.7:
        return "green"
    elif health >= 0.5:
        return "yellow"
    else:
        return "red"