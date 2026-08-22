from dataclasses import dataclass


@dataclass
class IntegratedInvestmentView:
    chews: int
    patients: int

    monthly_revenue: float
    annual_revenue: float
    monthly_chew_cost: float
    annual_chew_cost: float

    setup_cost: float
    annual_contribution: float

    investor_capital: float
    investor_value: float
    investor_gain: float
    investor_roi: float
    target_roi: float
    roi_gap: float
    investment_multiple: float
    decision: str


def build_integrated_investment_view(
    scenario,
    projection_totals,
    investor_return_analysis,
    investor_decision_metrics,
):
    return IntegratedInvestmentView(
        chews=scenario["chews"],
        patients=scenario["patients"],
        monthly_revenue=scenario["monthly_revenue"],
        annual_revenue=scenario["annual_revenue"],
        monthly_chew_cost=scenario["monthly_chew_cost"],
        annual_chew_cost=(
            scenario["monthly_chew_cost"] * 12
        ),
        setup_cost=scenario["confirmed_setup_cost"],
        annual_contribution=(
            scenario["monthly_contribution"] * 12
        ),
        investor_capital=(
            projection_totals["investor_capital"]
        ),
        investor_value=(
            investor_return_analysis.total_investor_value
        ),
        investor_gain=(
            investor_return_analysis.net_investor_gain
        ),
        investor_roi=(
            investor_decision_metrics["investor_roi"]
        ),
        target_roi=(
            investor_decision_metrics["target_roi"]
        ),
        roi_gap=(
            investor_decision_metrics["roi_gap"]
        ),
        investment_multiple=(
            investor_decision_metrics["investment_multiple"]
        ),
        decision=(
            investor_decision_metrics["decision"]
        ),
    )
