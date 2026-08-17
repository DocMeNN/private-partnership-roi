from pathlib import Path
import csv


# ============================================================
# EASEPAL CARE — V1 ASSUMPTION LOADER
# ============================================================

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

ASSUMPTIONS_FILE = DATA_DIR / "assumptions.csv"
COST_FILE = DATA_DIR / "cost_assumptions.csv"
SCENARIOS_FILE = DATA_DIR / "scenarios.csv"


def load_csv(filename):
    """
    Load a CSV file into a list of dictionaries.
    """
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def numeric(value):
    """
    Safely convert numeric CSV values.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def load_assumptions():
    """
    Load all assumptions from assumptions.csv.
    """

    rows = load_csv(ASSUMPTIONS_FILE)

    assumptions = {}

    for row in rows:

        variable = row["variable"]

        assumptions[variable] = {
            "value": numeric(row["value"]),
            "unit": row["unit"],
            "driver": row["driver"],
            "status": row["status"],
            "category": row["category"],
        }

    return assumptions


def load_costs():
    """
    Load cost assumptions.
    """

    rows = load_csv(COST_FILE)

    costs = []

    for row in rows:

        costs.append({
            "id": row["cost_id"],
            "category": row["cost_category"],
            "item": row["cost_item"],
            "driver": row["driver"],
            "amount": numeric(row["amount_ngn"]),
            "cost_type": row["cost_type"],
            "status": row["status"],
        })

    return costs


def load_scenarios():
    """
    Load predefined scaling scenarios.
    """

    rows = load_csv(SCENARIOS_FILE)

    scenarios = []

    for row in rows:

        scenarios.append({
            "id": row["scenario_id"],
            "chews": int(row["chews"]),
            "patients_per_chew": int(
                row["patients_per_chew"]
            ),
            "patients": int(row["patients"]),
        })

    return scenarios


# ============================================================
# LOAD V1 DATA
# ============================================================

ASSUMPTIONS = load_assumptions()
COSTS = load_costs()
SCENARIOS = load_scenarios()


# ============================================================
# EASY ACCESS TO CORE VARIABLES
# ============================================================

PATIENTS_PER_CHEW = int(
    ASSUMPTIONS[
        "Patients per CHEW"
    ]["value"]
)


SUBSCRIPTION_PRICE = ASSUMPTIONS[
    "Private subscription"
]["value"]


CHEW_REMUNERATION = ASSUMPTIONS[
    "CHEW monthly remuneration"
]["value"]


# ============================================================
# DATA STATUS HELPERS
# ============================================================

def confirmed_assumptions():

    return [
        item
        for item in ASSUMPTIONS.values()
        if item["status"] == "CONFIRMED"
    ]


def tbd_assumptions():

    return [
        item
        for item in ASSUMPTIONS.values()
        if item["status"] == "TBD"
    ]


def confirmed_costs():

    return [
        item
        for item in COSTS
        if item["status"] == "CONFIRMED"
    ]


def tbd_costs():

    return [
        item
        for item in COSTS
        if item["status"] == "TBD"
    ]


# ============================================================
# VALIDATION
# ============================================================

def validate_data():

    errors = []

    if PATIENTS_PER_CHEW <= 0:
        errors.append(
            "Patients per CHEW must be greater than zero."
        )

    if SUBSCRIPTION_PRICE < 0:
        errors.append(
            "Subscription price cannot be negative."
        )

    if CHEW_REMUNERATION < 0:
        errors.append(
            "CHEW remuneration cannot be negative."
        )

    if not SCENARIOS:
        errors.append(
            "No scaling scenarios found."
        )

    if errors:
        raise ValueError(
            "\n".join(errors)
        )

    return True


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    validate_data()

    print()
    print("=" * 65)
    print(" EASEPAL CARE — V1 DATA LAYER")
    print("=" * 65)
    print()

    print(
        f"Patients per CHEW       : {PATIENTS_PER_CHEW}"
    )

    print(
        f"Subscription             : ₦{SUBSCRIPTION_PRICE:,.0f}"
    )

    print(
        f"CHEW remuneration        : ₦{CHEW_REMUNERATION:,.0f}"
    )

    print()

    print(
        f"Confirmed assumptions    : "
        f"{len(confirmed_assumptions())}"
    )

    print(
        f"TBD assumptions          : "
        f"{len(tbd_assumptions())}"
    )

    print(
        f"Confirmed costs          : "
        f"{len(confirmed_costs())}"
    )

    print(
        f"TBD costs                : "
        f"{len(tbd_costs())}"
    )

    print()

    print(
        f"Scaling scenarios        : "
        f"{len(SCENARIOS)}"
    )

    print()

    print("DATA VALIDATION: PASSED")
    print("V1 assumptions successfully loaded from CSV.")
    print()
