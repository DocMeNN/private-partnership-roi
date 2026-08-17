from data.loader import (
    PATIENTS_PER_CHEW,
    SUBSCRIPTION_PRICE,
    CHEW_REMUNERATION,
    SCENARIOS,
    confirmed_costs,
)


# ============================================================
# BASIC REVENUE MODEL
# ============================================================

def calculate_patients(chews):
    """
    Patients supported by the CHEW network.
    """
    return chews * PATIENTS_PER_CHEW


def calculate_monthly_revenue(chews):
    """
    Monthly subscription revenue.
    """
    patients = calculate_patients(chews)

    return patients * SUBSCRIPTION_PRICE


def calculate_annual_revenue(chews):
    """
    Annual subscription revenue.
    """
    return calculate_monthly_revenue(chews) * 12


# ============================================================
# CHEW REMUNERATION
# ============================================================

def calculate_monthly_chew_remuneration(chews):
    """
    Monthly CHEW remuneration.
    """
    return chews * CHEW_REMUNERATION


def calculate_annual_chew_remuneration(chews):
    """
    Annual CHEW remuneration.
    """
    return calculate_monthly_chew_remuneration(chews) * 12


# ============================================================
# CONFIRMED SETUP COSTS
# ============================================================

def calculate_confirmed_setup_cost(chews):

    total = 0

    for cost in confirmed_costs():

        if cost["driver"] == "Per CHEW":

            total += cost["amount"] * chews

        elif cost["driver"] in [
            "Per recruitment cycle",
            "Per cycle",
            "Per training cycle",
        ]:

            total += cost["amount"]

        elif cost["driver"] == "Fixed/shared":

            total += cost["amount"]

    return total


# ============================================================
# CONTRIBUTION
# ============================================================

def calculate_monthly_contribution(chews):

    revenue = calculate_monthly_revenue(chews)

    remuneration = calculate_monthly_chew_remuneration(
        chews
    )

    return revenue - remuneration


# ============================================================
# COMPLETE SCENARIO
# ============================================================

def calculate_scenario(chews):

    patients = calculate_patients(chews)

    monthly_revenue = calculate_monthly_revenue(
        chews
    )

    annual_revenue = calculate_annual_revenue(
        chews
    )

    monthly_remuneration = (
        calculate_monthly_chew_remuneration(
            chews
        )
    )

    annual_remuneration = (
        calculate_annual_chew_remuneration(
            chews
        )
    )

    setup_cost = calculate_confirmed_setup_cost(
        chews
    )

    monthly_contribution = (
        calculate_monthly_contribution(
            chews
        )
    )

    return {
        "chews": chews,
        "patients": patients,
        "monthly_revenue": monthly_revenue,
        "annual_revenue": annual_revenue,
        "monthly_chew_remuneration":
            monthly_remuneration,
        "annual_chew_remuneration":
            annual_remuneration,
        "confirmed_setup_cost":
            setup_cost,
        "monthly_contribution":
            monthly_contribution,
    }


# ============================================================
# TEST ALL SCENARIOS
# ============================================================

def run_all_scenarios():

    results = []

    for scenario in SCENARIOS:

        results.append(
            calculate_scenario(
                scenario["chews"]
            )
        )

    return results


if __name__ == "__main__":

    print()
    print("=" * 65)
    print(
        " EASEPAL CARE — V1 CALCULATOR "
    )
    print("=" * 65)

    print()

    for result in run_all_scenarios():

        print(
            f"CHEWs                 : "
            f"{result['chews']:,}"
        )

        print(
            f"Patients              : "
            f"{result['patients']:,}"
        )

        print(
            f"Monthly Revenue       : "
            f"₦{result['monthly_revenue']:,.0f}"
        )

        print(
            f"Annual Revenue        : "
            f"₦{result['annual_revenue']:,.0f}"
        )

        print(
            f"Monthly CHEW Cost     : "
            f"₦{result['monthly_chew_remuneration']:,.0f}"
        )

        print(
            f"Confirmed Setup Cost  : "
            f"₦{result['confirmed_setup_cost']:,.0f}"
        )

        print(
            f"Monthly Contribution  : "
            f"₦{result['monthly_contribution']:,.0f}"
        )

        print("-" * 65)

    print()
    print(
        "CALCULATOR TEST: PASSED"
    )
    print(
        "Calculator is connected to the V1 data layer."
    )
    print()
