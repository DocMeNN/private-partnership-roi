from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.investment_assumptions import InvestmentAssumptions
from dashboard.v2.projection_engine import (
    project_five_years,
    calculate_five_year_totals,
)


def test_five_year_projection_100_chews():
    assumptions = InvestmentAssumptions(
        investor_capital=50_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=1.0,
        repayment_period_years=5,
        ownership_percentage=20.0,
    )

    projection = project_five_years(100, assumptions)
    totals = calculate_five_year_totals(projection)

    assert len(projection) == 5
    assert totals["total_revenue"] == 900_000_000
    assert totals["total_chew_cost"] == 660_000_000
    assert totals["total_contribution"] == 240_000_000
    assert totals["investor_capital"] == 50_000_000
