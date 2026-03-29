from app.models.ml.health_score import compute_health_score, classify_health_score

def test_health_score():
    assert compute_health_score(1.0, 1.0, 1.0) == 1.0
    assert compute_health_score(0.5, 0.5, 0.5) == 0.5

def test_classify():
    assert classify_health_score(0.8) == "green"
    assert classify_health_score(0.6) == "yellow"
    assert classify_health_score(0.4) == "red"