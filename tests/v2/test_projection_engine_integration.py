from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
)
from dashboard.v2.projection_engine import (
    project_five_years,
    calculate_five_year_totals,
)


def test_projection_engine_import():
    assert callable(project_five_years)
    assert callable(calculate_five_year_totals)


def test_projection_engine_returns_five_years():
    assumptions = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    projection = project_five_years(10, assumptions)

    assert len(projection) == 5
    assert [row["year"] for row in projection] == [1, 2, 3, 4, 5]


def test_projection_totals():
    assumptions = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    projection = project_five_years(10, assumptions)
    totals = calculate_five_year_totals(projection)

    assert totals["total_revenue"] == 90_000_000
    assert totals["total_chew_cost"] == 66_000_000
    assert totals["total_contribution"] == 24_000_000
    assert totals["investor_capital"] == 10_000_000
