from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
    create_default_assumptions,
    validate_assumptions,
)


def test_default_assumptions():
    assumptions = create_default_assumptions()

    assert assumptions.investment_period_years == 5
    assert assumptions.investor_return_target == 0.20
    assert assumptions.financing_type == "Equity"


def test_valid_assumptions():
    assumptions = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )

    assert validate_assumptions(assumptions) == []


def test_invalid_assumptions():
    assumptions = InvestmentAssumptions(
        investor_capital=-1,
        investment_period_years=0,
        investor_return_target=1.5,
        exit_multiple=-1,
        repayment_period_years=0,
        ownership_percentage=101,
    )

    errors = validate_assumptions(assumptions)

    assert len(errors) == 6
