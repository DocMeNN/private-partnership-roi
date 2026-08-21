from dataclasses import dataclass


@dataclass
class InvestorReturnAnalysis:
    investor_capital: float
    total_contribution: float
    investor_return_target: float
    ownership_percentage: float
    exit_multiple: float

    @property
    def target_return(self) -> float:
        return (
            self.investor_capital
            * self.investor_return_target
        )

    @property
    def investor_share_of_contribution(self) -> float:
        return (
            self.total_contribution
            * self.ownership_percentage
            / 100
        )

    @property
    def exit_value(self) -> float:
        return (
            self.investor_capital
            * self.exit_multiple
        )

    @property
    def total_investor_value(self) -> float:
        return (
            self.investor_share_of_contribution
            + self.exit_value
        )

    @property
    def net_investor_gain(self) -> float:
        return (
            self.total_investor_value
            - self.investor_capital
        )

    @property
    def roi_percentage(self) -> float:
        if self.investor_capital <= 0:
            return 0.0

        return (
            self.net_investor_gain
            / self.investor_capital
        ) * 100


def calculate_investor_return(
    investor_capital: float,
    total_contribution: float,
    investor_return_target: float,
    ownership_percentage: float,
    exit_multiple: float,
) -> InvestorReturnAnalysis:

    return InvestorReturnAnalysis(
        investor_capital=investor_capital,
        total_contribution=total_contribution,
        investor_return_target=investor_return_target,
        ownership_percentage=ownership_percentage,
        exit_multiple=exit_multiple,
    )
