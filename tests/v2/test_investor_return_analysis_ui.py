from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
)
from dashboard.v2.investor_return_analysis_ui import (
    render_investor_return_analysis,
)


def test_investor_return_dashboard_logic():
    assumptions = InvestmentAssumptions(
        investor_capital=50_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=1.0,
        repayment_period_years=5,
        ownership_percentage=20.0,
    )

    assert assumptions.investor_capital == 50_000_000
    assert assumptions.ownership_percentage == 20.0
    assert assumptions.exit_multiple == 1.0
