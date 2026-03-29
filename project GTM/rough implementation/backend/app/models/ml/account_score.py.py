# backend/app/models/ml/account_score.py

def compute_score(intent: float, usage: float, icp: float) -> float:
    """Account Score = 0.4*intent + 0.3*usage + 0.3*icp"""
    return 0.4 * intent + 0.3 * usage + 0.3 * icp