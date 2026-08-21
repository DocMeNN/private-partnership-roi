from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
    validate_assumptions,
)

def test_valid_equity_assumptions():
    a = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )
    assert validate_assumptions(a) == []

def test_zero_capital_is_invalid():
    a = InvestmentAssumptions(
        investor_capital=0,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )
    assert validate_assumptions(a)

def test_equity_zero_ownership_is_invalid():
    a = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=0.20,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=0,
    )
    assert validate_assumptions(a)

def test_return_above_100_is_invalid():
    a = InvestmentAssumptions(
        investor_capital=10_000_000,
        investment_period_years=5,
        investor_return_target=1.01,
        financing_type="Equity",
        exit_multiple=2.0,
        repayment_period_years=5,
        ownership_percentage=25,
    )
    assert validate_assumptions(a)
