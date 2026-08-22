from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
)
from dashboard.v2.investor_return_analysis import (
    calculate_investor_return,
)
from dashboard.v2.investor_decision_metrics import (
    calculate_decision_metrics,
)


def test_decision_metrics_dashboard_layer():

    assumptions = InvestmentAssumptions(
        investor_capital=50_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=1.0,
        repayment_period_years=5,
        ownership_percentage=20.0,
    )

    analysis = calculate_investor_return(
        investor_capital=assumptions.investor_capital,
        total_contribution=240_000_000,
        investor_return_target=assumptions.investor_return_target,
        ownership_percentage=assumptions.ownership_percentage,
        exit_multiple=assumptions.exit_multiple,
    )

    metrics = calculate_decision_metrics(
        investor_capital=assumptions.investor_capital,
        total_contribution=240_000_000,
        investor_return_target=assumptions.investor_return_target,
        ownership_percentage=assumptions.ownership_percentage,
        exit_multiple=assumptions.exit_multiple,
        investor_roi=analysis.roi_percentage,
    )

    assert metrics["investor_roi"] == 96.0
    assert metrics["target_roi"] == 20.0
    assert metrics["roi_gap"] == 76.0
    assert metrics["investment_multiple"] == 1.96
    assert metrics["capital_required"] == 50_000_000
    assert metrics["investor_value"] == 98_000_000
    assert metrics["net_gain"] == 48_000_000
    assert metrics["decision"] == "ATTRACTIVE"
