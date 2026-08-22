from dataclasses import dataclass

from dashboard.v2.investor_return_analysis import (
    calculate_investor_return,
)


@dataclass
class InvestorDecisionMetrics:
    investor_capital: float
    total_contribution: float
    net_investor_gain: float
    total_investor_value: float
    investor_return_target: float

    @property
    def investment_multiple(self) -> float:
        if self.investor_capital <= 0:
            return 0.0

        return (
            self.total_investor_value
            / self.investor_capital
        )

    @property
    def payback_period_years(self) -> float:
        if self.net_investor_gain <= 0:
            return float("inf")

        annual_gain = self.net_investor_gain / 5

        if annual_gain <= 0:
            return float("inf")

        return self.investor_capital / annual_gain

    @property
    def contribution_to_capital_ratio(self) -> float:
        if self.investor_capital <= 0:
            return 0.0

        return (
            self.total_contribution
            / self.investor_capital
        )

    @property
    def target_return_value(self) -> float:
        return (
            self.investor_capital
            * self.investor_return_target
        )

    @property
    def target_return_gap(self) -> float:
        return (
            self.net_investor_gain
            - self.target_return_value
        )

    @property
    def target_return_met(self) -> bool:
        return (
            self.net_investor_gain
            >= self.target_return_value
        )


def calculate_investor_decision_metrics(
    investor_capital: float,
    total_contribution: float,
    net_investor_gain: float,
    total_investor_value: float,
    investor_return_target: float,
) -> InvestorDecisionMetrics:

    return InvestorDecisionMetrics(
        investor_capital=investor_capital,
        total_contribution=total_contribution,
        net_investor_gain=net_investor_gain,
        total_investor_value=total_investor_value,
        investor_return_target=investor_return_target,
    )


def calculate_decision_metrics(
    investor_capital: float,
    total_contribution: float,
    investor_return_target: float,
    ownership_percentage: float,
    exit_multiple: float,
    investor_roi: float,
):
    analysis = calculate_investor_return(
        investor_capital=investor_capital,
        total_contribution=total_contribution,
        investor_return_target=investor_return_target,
        ownership_percentage=ownership_percentage,
        exit_multiple=exit_multiple,
    )

    target_roi = investor_return_target * 100
    roi_gap = investor_roi - target_roi

    if investor_capital <= 0:
        investment_multiple = 0.0
    else:
        investment_multiple = (
            analysis.total_investor_value
            / investor_capital
        )

    if investor_roi >= target_roi:
        decision = "ATTRACTIVE"
    elif investor_roi >= target_roi * 0.75:
        decision = "BORDERLINE"
    else:
        decision = "UNATTRACTIVE"

    return {
        "investor_roi": investor_roi,
        "target_roi": target_roi,
        "roi_gap": roi_gap,
        "investment_multiple": round(
            investment_multiple,
            2,
        ),
        "capital_required": investor_capital,
        "investor_value": analysis.total_investor_value,
        "net_gain": analysis.net_investor_gain,
        "decision": decision,
    }
