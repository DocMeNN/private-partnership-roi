"""
V2 Investment Assumptions Interface
Editable Streamlit interface for investor and financing assumptions.
"""

import streamlit as st

from dashboard.v2.investment_assumptions import (
    InvestmentAssumptions,
    validate_assumptions,
)


def render_investment_assumptions():
    st.subheader("Investment Assumptions")

    st.caption(
        "Enter the investment structure that will drive the V2 financial projection."
    )

    col1, col2 = st.columns(2)

    with col1:
        investor_capital = st.number_input(
            "Investor Capital (₦)",
            min_value=0.0,
            value=0.0,
            step=100000.0,
            format="%.0f",
        )

        investment_period_years = st.number_input(
            "Investment Period (Years)",
            min_value=1,
            value=5,
            step=1,
        )

        investor_return_target = st.number_input(
            "Target Investor Return (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=1.0,
        )

        financing_type = st.selectbox(
            "Financing Type",
            [
                "Equity",
                "Debt",
                "Convertible",
                "Revenue Share",
                "Hybrid",
            ],
        )

    with col2:
        ownership_percentage = st.number_input(
            "Investor Ownership (%)",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=1.0,
        )

        exit_multiple = st.number_input(
            "Exit Multiple",
            min_value=0.0,
            value=1.0,
            step=0.1,
        )

        repayment_period_years = st.number_input(
            "Repayment Period (Years)",
            min_value=1,
            value=5,
            step=1,
        )

    assumptions = InvestmentAssumptions(
        investor_capital=investor_capital,
        investment_period_years=investment_period_years,
        investor_return_target=investor_return_target / 100,
        financing_type=financing_type,
        exit_multiple=exit_multiple,
        repayment_period_years=repayment_period_years,
        ownership_percentage=ownership_percentage,
    )

    errors = validate_assumptions(assumptions)

    if errors:
        for error in errors:
            st.error(error)
    else:
        st.success("Investment assumptions are valid.")

    return assumptions
