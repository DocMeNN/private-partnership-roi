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


def test_investor_economics_integration():

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

    assert analysis.target_return == 10_000_000
    assert analysis.investor_share_of_contribution == 48_000_000
    assert analysis.exit_value == 50_000_000
    assert analysis.total_investor_value == 98_000_000
    assert analysis.net_investor_gain == 48_000_000
    assert analysis.roi_percentage == 96.0
