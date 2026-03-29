from app.models.ml.account_score import compute_score

def test_compute_score():
    assert compute_score(1.0, 1.0, 1.0) == 1.0
    assert compute_score(0.5, 0.5, 0.5) == 0.5
    assert 0.4*0.8 + 0.3*0.6 + 0.3*0.4 == compute_score(0.8, 0.6, 0.4)