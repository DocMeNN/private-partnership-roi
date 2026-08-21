from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
    validate_assumptions,
)
from dashboard.v2.investment_assumptions_ui import render_investment_assumptions


def test_ui_module_imports():
    assert callable(render_investment_assumptions)


def test_ui_assumptions_model():
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
