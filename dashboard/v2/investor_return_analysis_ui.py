import streamlit as st

from dashboard.v2.investor_return_analysis import (
    calculate_investor_return,
)


def render_investor_return_analysis(
    investment_assumptions,
    total_contribution,
):
    st.subheader("Investor Return Analysis")

    analysis = calculate_investor_return(
        investor_capital=investment_assumptions.investor_capital,
        total_contribution=total_contribution,
        investor_return_target=investment_assumptions.investor_return_target,
        ownership_percentage=investment_assumptions.ownership_percentage,
        exit_multiple=investment_assumptions.exit_multiple,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Target Investor Return",
            f"?{analysis.target_return:,.0f}",
        )

    with c2:
        st.metric(
            "Investor Share of Contribution",
            f"?{analysis.investor_share_of_contribution:,.0f}",
        )

    with c3:
        st.metric(
            "Exit Value",
            f"?{analysis.exit_value:,.0f}",
        )

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "Total Investor Value",
            f"?{analysis.total_investor_value:,.0f}",
        )

    with c5:
        st.metric(
            "Net Investor Gain",
            f"?{analysis.net_investor_gain:,.0f}",
        )

    with c6:
        st.metric(
            "Investor ROI",
            f"{analysis.roi_percentage:,.1f}%",
        )

    if analysis.roi_percentage >= (
        investment_assumptions.investor_return_target * 100
    ):
        st.success(
            "Investor return currently meets or exceeds the target."
        )
    else:
        st.warning(
            "Investor return is currently below the target."
        )

    return analysis
