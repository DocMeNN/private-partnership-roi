from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
)
from dashboard.v2.projection_engine import (
    project_five_years,
    calculate_five_year_totals,
)


def test_five_year_projection_has_five_rows():

    assumptions = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    projection = project_five_years(
        10,
        assumptions,
    )

    assert len(projection) == 5


def test_projection_uses_v1_revenue_model():

    assumptions = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    projection = project_five_years(
        10,
        assumptions,
    )

    assert projection[0]["annual_revenue"] == 18_000_000
    assert projection[0]["annual_chew_cost"] == 13_200_000
    assert projection[0]["annual_contribution"] == 4_800_000


def test_investor_capital_is_recorded_once():

    assumptions = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    projection = project_five_years(
        10,
        assumptions,
    )

    assert projection[0]["investor_capital"] == 10_000_000
    assert all(
        row["investor_capital"] == 0
        for row in projection[1:]
    )


def test_five_year_totals():

    assumptions = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    projection = project_five_years(
        10,
        assumptions,
    )

    totals = calculate_five_year_totals(
        projection
    )

    assert totals["total_revenue"] == 90_000_000
    assert totals["total_chew_cost"] == 66_000_000
    assert totals["total_contribution"] == 24_000_000
    assert totals["investor_capital"] == 10_000_000


def test_invalid_assumptions_are_rejected():

    assumptions = InvestmentAssumptions(
        investor_capital=0,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    try:
        project_five_years(
            10,
            assumptions,
        )
        assert False
    except ValueError:
        assert True
