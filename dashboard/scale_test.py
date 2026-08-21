from dashboard.calculator import calculate_scenario


def test_scale_calculation():
    result = calculate_scenario(10)

    assert result["chews"] == 10
    assert result["patients"] == 100
