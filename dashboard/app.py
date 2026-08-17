import streamlit as st
import csv
from pathlib import Path

from dashboard.calculator import calculate_scenario
from data.loader import (
    PATIENTS_PER_CHEW,
    SUBSCRIPTION_PRICE,
    CHEW_REMUNERATION,
    SCENARIOS,
)


# ============================================================
# PATHS
# ============================================================

ROOT = Path(__file__).resolve().parent.parent

ASSUMPTIONS_FILE = (
    ROOT / "data" / "assumptions.csv"
)


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="EasePal Care — Private Partnership ROI",
    page_icon="📊",
    layout="wide",
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "EasePal Care — Private Partnership ROI & Scaling Dashboard"
)

st.caption(
    "Version 1.0 | Editable Financial Assumptions"
)

st.divider()


# ============================================================
# LOAD ASSUMPTIONS
# ============================================================

def load_assumptions():

    with open(
        ASSUMPTIONS_FILE,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        return list(
            csv.DictReader(file)
        )


def save_assumptions(rows):

    fieldnames = [
        "assumption_id",
        "category",
        "variable",
        "value",
        "unit",
        "driver",
        "status",
        "source_note",
    ]

    with open(
        ASSUMPTIONS_FILE,
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(rows)


# ============================================================
# SESSION STATE
# ============================================================

if "assumptions" not in st.session_state:

    st.session_state.assumptions = (
        load_assumptions()
    )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "Scenario Selection"
)

scenario_values = [
    s["chews"]
    for s in SCENARIOS
]

selected_chews = st.sidebar.selectbox(
    "Number of CHEWs",
    scenario_values,
)


st.sidebar.divider()

st.sidebar.markdown(
    "### Current Model"
)

st.sidebar.write(
    f"Patients/CHEW: **{PATIENTS_PER_CHEW}**"
)

st.sidebar.write(
    f"Subscription: **₦{SUBSCRIPTION_PRICE:,.0f}**"
)

st.sidebar.write(
    f"CHEW remuneration: **₦{CHEW_REMUNERATION:,.0f}**"
)


# ============================================================
# ASSUMPTIONS EDITOR
# ============================================================

st.header(
    "Editable Cost & Revenue Assumptions"
)

st.info(
    "Enter values for TBD assumptions directly here. "
    "Click 'Save Assumptions' to write the updated "
    "values to the project's data file."
)


rows = st.session_state.assumptions


# ============================================================
# CATEGORY GROUPING
# ============================================================

categories = []

for row in rows:

    category = row["category"]

    if category not in categories:

        categories.append(category)


updated_rows = []


for category in categories:

    st.subheader(category)

    category_rows = [
        r for r in rows
        if r["category"] == category
    ]

    for row in category_rows:

        current_value = row["value"]

        try:
            numeric_value = float(
                current_value
            )
        except:
            numeric_value = 0.0


        col1, col2, col3, col4 = st.columns(
            [3, 1.5, 1.5, 2]
        )


        with col1:

            st.write(
                f"**{row['variable']}**"
            )


        with col2:

            st.caption(
                row["driver"]
            )


        with col3:

            new_value = st.number_input(
                "Value",
                min_value=0.0,
                value=numeric_value,
                step=1000.0,
                key=f"value_{row['assumption_id']}",
                label_visibility="collapsed",
            )


        with col4:

            status = row["status"]

            if status == "CONFIRMED":

                st.success(
                    "CONFIRMED"
                )

            else:

                st.warning(
                    "TBD"
                )


        row_copy = row.copy()

        row_copy["value"] = str(
            new_value
        )

        updated_rows.append(
            row_copy
        )


    st.divider()


# ============================================================
# SAVE
# ============================================================

if st.button(
    "💾 Save Assumptions",
    type="primary",
    use_container_width=True,
):

    save_assumptions(
        updated_rows
    )

    st.session_state.assumptions = (
        updated_rows
    )

    st.success(
        "Assumptions saved successfully."
    )

    st.rerun()


# ============================================================
# CALCULATOR
# ============================================================

st.header(
    f"Scaling Result — {selected_chews:,} CHEWs"
)


result = calculate_scenario(
    selected_chews
)


patients = result["patients"]

monthly_revenue = (
    result["monthly_revenue"]
)

annual_revenue = (
    result["annual_revenue"]
)

monthly_chew_cost = (
    result["monthly_chew_remuneration"]
)

setup_cost = (
    result["confirmed_setup_cost"]
)

monthly_contribution = (
    result["monthly_contribution"]
)

annual_contribution = (
    monthly_contribution * 12
)


# ============================================================
# KPI CARDS
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "CHEWs",
        f"{selected_chews:,}"
    )

with c2:

    st.metric(
        "Patients",
        f"{patients:,}"
    )

with c3:

    st.metric(
        "Monthly Revenue",
        f"₦{monthly_revenue:,.0f}"
    )

with c4:

    st.metric(
        "Annual Revenue",
        f"₦{annual_revenue:,.0f}"
    )


c5, c6, c7, c8 = st.columns(4)

with c5:

    st.metric(
        "Confirmed Setup Cost",
        f"₦{setup_cost:,.0f}"
    )

with c6:

    st.metric(
        "Monthly CHEW Cost",
        f"₦{monthly_chew_cost:,.0f}"
    )

with c7:

    st.metric(
        "Monthly Contribution",
        f"₦{monthly_contribution:,.0f}"
    )

with c8:

    st.metric(
        "Annual Contribution",
        f"₦{annual_contribution:,.0f}"
    )


st.divider()


# ============================================================
# SCALING TABLE
# ============================================================

st.header(
    "Scaling Scenarios"
)

table = []

for scenario in SCENARIOS:

    r = calculate_scenario(
        scenario["chews"]
    )

    table.append({

        "CHEWs":
            r["chews"],

        "Patients":
            r["patients"],

        "Monthly Revenue":
            f"₦{r['monthly_revenue']:,.0f}",

        "Annual Revenue":
            f"₦{r['annual_revenue']:,.0f}",

        "Confirmed Setup Cost":
            f"₦{r['confirmed_setup_cost']:,.0f}",

        "Monthly Contribution":
            f"₦{r['monthly_contribution']:,.0f}",
    })


st.dataframe(
    table,
    use_container_width=True,
    hide_index=True,
)


st.divider()


# ============================================================
# MODEL WARNING
# ============================================================

st.warning(
    "IMPORTANT: TBD values can now be entered and saved "
    "through this dashboard. The current calculator engine "
    "will continue to use only assumptions explicitly "
    "incorporated into its formulas. We will connect all "
    "additional cost categories to the mathematical model "
    "in the next modelling pass."
)


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "EasePal Care | Private Partnership ROI & Scaling Dashboard | V1.0"
)
