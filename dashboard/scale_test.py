from calculator import calculate
from assumptions import SCALING_LEVELS, PATIENTS_PER_CHEW, SUBSCRIPTION_PER_PATIENT_MONTH, CHEW_MONTHLY_REMUNERATION


def money(value):
    return f"₦{value:,.0f}"


print()
print("=" * 100)
print(" EASEPAL CARE — V1 SCALE TEST")
print("=" * 100)
print()

print("Testing all approved CHEW scaling scenarios:")
print("10 → 50 → 100 → 200 → 500 → 1,000 → 2,000 → 5,000")
print()

all_passed = True


for chews in SCALING_LEVELS:

    result = calculate(chews)

    expected_patients = chews * PATIENTS_PER_CHEW
    expected_monthly_revenue = (
        expected_patients * SUBSCRIPTION_PER_PATIENT_MONTH
    )
    expected_annual_revenue = (
        expected_monthly_revenue * 12
    )
    expected_monthly_chew_cost = (
        chews * CHEW_MONTHLY_REMUNERATION
    )
    expected_monthly_contribution = (
        expected_monthly_revenue
        - expected_monthly_chew_cost
    )

    patients_ok = (
        result["patients"] == expected_patients
    )

    monthly_revenue_ok = (
        result["monthly_revenue"]
        == expected_monthly_revenue
    )

    annual_revenue_ok = (
        result["annual_revenue"]
        == expected_annual_revenue
    )

    chew_cost_ok = (
        result["monthly_chew_remuneration"]
        == expected_monthly_chew_cost
    )

    contribution_ok = (
        result["preliminary_monthly_contribution"]
        == expected_monthly_contribution
    )

    passed = all([
        patients_ok,
        monthly_revenue_ok,
        annual_revenue_ok,
        chew_cost_ok,
        contribution_ok,
    ])

    if not passed:
        all_passed = False

    status = "PASS" if passed else "FAIL"

    print("-" * 100)

    print(f"CHEWs                  : {chews:,}")
    print(f"Patients               : {result['patients']:,}")
    print(f"Monthly Revenue        : {money(result['monthly_revenue'])}")
    print(f"Annual Revenue         : {money(result['annual_revenue'])}")
    print(f"Monthly CHEW Cost      : {money(result['monthly_chew_remuneration'])}")
    print(f"Setup Cost             : {money(result['confirmed_setup_cost'])}")
    print(
        f"Monthly Contribution  : "
        f"{money(result['preliminary_monthly_contribution'])}"
    )
    print(f"TEST RESULT            : {status}")


print()
print("=" * 100)

if all_passed:
    print("OVERALL RESULT: ALL SCALE TESTS PASSED")
else:
    print("OVERALL RESULT: ONE OR MORE TESTS FAILED")

print("=" * 100)
print()

print("FORMULA CHECKS")
print("-" * 100)

print("Patients = CHEWs × Patients/CHEW")
print("Revenue = Patients × Subscription Price")
print("Annual Revenue = Monthly Revenue × 12")
print("CHEW Cost = CHEWs × Monthly CHEW Remuneration")
print("Contribution = Revenue − CHEW Cost")

print()
print("NOTE:")
print("TBD operating costs are intentionally excluded.")
print("This test validates the current mathematical engine only.")
print()
