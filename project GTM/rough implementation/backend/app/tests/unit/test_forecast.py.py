import pandas as pd
from app.models.ml.forecast import predict_quarterly

def test_predict_quarterly():
    data = pd.DataFrame({
        'amount': [10000, 20000],
        'win_probability': [0.5, 0.8]
    })
    result = predict_quarterly(data)
    assert result == 10000*0.5 + 20000*0.8
    assert predict_quarterly(pd.DataFrame()) == 0.0