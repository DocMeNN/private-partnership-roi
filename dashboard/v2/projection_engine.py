"""
V2 Five-Year Projection Engine
Builds a five-year financial projection from the confirmed V1 model
and investor assumptions.
"""

from dashboard.calculator import (
    calculate_scenario,
)
from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
    validate_assumptions,
)


def project_five_years(
    chews: int,
    assumptions: InvestmentAssumptions,
) -> list[dict]:
    """
    Generate annual five-year projections.

    V1 revenue and CHEW remuneration remain the base operating model.
    Investor assumptions provide the financing context.
    """

    errors = validate_assumptions(assumptions)

    if errors:
        raise ValueError("\n".join(errors))

    scenario = calculate_scenario(chews)

    annual_revenue = scenario["annual_revenue"]
    annual_chew_cost = scenario["annual_chew_remuneration"]
    annual_contribution = (
        annual_revenue - annual_chew_cost
    )

    projection = []

    for year in range(
        1,
        assumptions.investment_period_years + 1,
    ):
        projection.append(
            {
                "year": year,
                "chews": chews,
                "patients": scenario["patients"],
                "annual_revenue": annual_revenue,
                "annual_chew_cost": annual_chew_cost,
                "annual_contribution": annual_contribution,
                "investor_capital": (
                    assumptions.investor_capital
                    if year == 1
                    else 0
                ),
            }
        )

    return projection


def calculate_five_year_totals(
    projection: list[dict],
) -> dict:
    """
    Aggregate the five-year projection.
    """

    return {
        "total_revenue": sum(
            row["annual_revenue"]
            for row in projection
        ),
        "total_chew_cost": sum(
            row["annual_chew_cost"]
            for row in projection
        ),
        "total_contribution": sum(
            row["annual_contribution"]
            for row in projection
        ),
        "investor_capital": sum(
            row["investor_capital"]
            for row in projection
        ),
    }
