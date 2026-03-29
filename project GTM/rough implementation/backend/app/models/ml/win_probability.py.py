# backend/app/models/ml/win_probability.py
import numpy as np

def predict_win_probability(stage: str, segment: str, region: str, days_in_stage: int, macro_index: float) -> float:
    """
    A logit model of the probability of deal closure.
     This is a simplified placeholder..
    """
    # coefficients (example)
    intercept = -2.1
    stage_coeff = {"Prospecting": 0.0, "Qualification": 0.8, "Proposal": 1.5, "Negotiation": 2.0}
    segment_coeff = {"Enterprise": 0.6, "MidMarket": 0.3, "SMB": 0.0}
    region_coeff = {"US": 0.2, "EMEA": -0.1, "APAC": -0.2, "LATAM": -0.3}
    days_coeff = 0.3
    macro_coeff = 0.5

    logit = intercept
    logit += stage_coeff.get(stage, 0)
    logit += segment_coeff.get(segment, 0)
    logit += region_coeff.get(region, 0)
    logit += days_coeff * np.log(days_in_stage + 1)
    logit += macro_coeff * macro_index

    prob = 1 / (1 + np.exp(-logit))
    return prob