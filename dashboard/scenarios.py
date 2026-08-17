from assumptions import SCALING_LEVELS
from calculator import calculate


def build_scenarios():

    scenarios = []

    for chews in SCALING_LEVELS:
        scenarios.append(calculate(chews))

    return scenarios


if __name__ == "__main__":

    for scenario in build_scenarios():

        print("=" * 60)
        print(f"CHEWs: {scenario['chews']:,}")
        print(f"Patients: {scenario['patients']:,}")
        print(
            f"Monthly Revenue: "
            f"₦{scenario['monthly_revenue']:,.0f}"
        )
        print(
            f"Annual Revenue: "
            f"₦{scenario['annual_revenue']:,.0f}"
        )
        print(
            f"Monthly CHEW Remuneration: "
            f"₦{scenario['monthly_chew_remuneration']:,.0f}"
        )
        print(
            f"Confirmed Setup Cost: "
            f"₦{scenario['confirmed_setup_cost']:,.0f}"
        )
        print(
            f"Preliminary Monthly Contribution: "
            f"₦{scenario['preliminary_monthly_contribution']:,.0f}"
        )
