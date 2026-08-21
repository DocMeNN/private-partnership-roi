"""
V2 Investment Assumptions
Editable investment and financing assumptions for the Yv-Me ROI model.
"""

from dataclasses import dataclass


@dataclass
class InvestmentAssumptions:
    investor_capital: float = 0.0
    investment_period_years: int = 5
    investor_return_target: float = 0.20
    financing_type: str = "Equity"
    exit_multiple: float = 1.0
    repayment_period_years: int = 5
    ownership_percentage: float = 0.0


def create_default_assumptions() -> InvestmentAssumptions:
    return InvestmentAssumptions()


def validate_assumptions(assumptions: InvestmentAssumptions) -> list[str]:
    errors = []

    if assumptions.investor_capital <= 0:
        errors.append("Investor capital must be greater than zero.")

    if assumptions.investment_period_years <= 0:
        errors.append("Investment period must be greater than zero.")

    if not 0 <= assumptions.investor_return_target <= 1:
        errors.append("Investor return target must be between 0% and 100%.")

    if assumptions.exit_multiple <= 0:
        errors.append("Exit multiple must be greater than zero.")

    if assumptions.repayment_period_years <= 0:
        errors.append("Repayment period must be greater than zero.")

    if not 0 <= assumptions.ownership_percentage <= 100:
        errors.append("Ownership percentage must be between 0% and 100%.")

    if assumptions.financing_type == "Equity" and assumptions.ownership_percentage <= 0:
        errors.append(
            "Equity financing requires investor ownership greater than 0%."
        )

    return errors
