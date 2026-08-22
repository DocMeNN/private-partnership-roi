from dataclasses import dataclass


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

        annual_gain = (
            self.net_investor_gain
            / 5
        )

        if annual_gain <= 0:
            return float("inf")

        return (
            self.investor_capital
            / annual_gain
        )

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
