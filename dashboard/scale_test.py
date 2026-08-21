from dashboard.calculator import calculate


def test_scale_calculation():
    result = calculate(10)

    assert result["chews"] == 10
