# backend/app/models/ml/forecast.py
import numpy as np
import pandas as pd

def predict_quarterly(pipeline_data: pd.DataFrame) -> float:
    """
    A simplified revenue forecast model based on a weighted pipeline.
    In reality, this would involve logistic regression + VAR.
    """
    if pipeline_data.empty:
        return 0.0
    # We assume that there are columns amount and win_probability
    forecast = (pipeline_data['amount'] * pipeline_data['win_probability']).sum()
    return forecast