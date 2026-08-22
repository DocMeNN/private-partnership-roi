from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.investor_decision_metrics import (
    calculate_investor_decision_metrics,
)


def test_investor_decision_metrics():

    metrics = calculate_investor_decision_metrics(
        investor_capital=50_000_000,
        total_contribution=240_000_000,
        net_investor_gain=48_000_000,
        total_investor_value=98_000_000,
        investor_return_target=0.20,
    )

    assert metrics.investment_multiple == 1.96
    assert metrics.payback_period_years == 5.208333333333333
    assert metrics.contribution_to_capital_ratio == 4.8
    assert metrics.target_return_value == 10_000_000
    assert metrics.target_return_gap == 38_000_000
    assert metrics.target_return_met is True


def test_zero_capital_is_safe():

    metrics = calculate_investor_decision_metrics(
        investor_capital=0,
        total_contribution=100_000_000,
        net_investor_gain=10_000_000,
        total_investor_value=10_000_000,
        investor_return_target=0.20,
    )

    assert metrics.investment_multiple == 0.0
    assert metrics.contribution_to_capital_ratio == 0.0
