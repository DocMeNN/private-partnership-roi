import streamlit as st

from dashboard.v2.investor_decision_metrics import (
    calculate_decision_metrics,
)


def render_investor_decision_metrics(
    investment_assumptions,
    investor_return_analysis,
    total_contribution,
):
    st.subheader("Investor Decision Metrics")

    metrics = calculate_decision_metrics(
        investor_capital=investment_assumptions.investor_capital,
        total_contribution=total_contribution,
        investor_return_target=(
            investment_assumptions.investor_return_target
        ),
        ownership_percentage=(
            investment_assumptions.ownership_percentage
        ),
        exit_multiple=investment_assumptions.exit_multiple,
        investor_roi=investor_return_analysis.roi_percentage,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Investor ROI",
            f"{metrics['investor_roi']:,.1f}%",
        )

    with c2:
        st.metric(
            "Target ROI",
            f"{metrics['target_roi']:,.1f}%",
        )

    with c3:
        st.metric(
            "ROI Gap",
            f"{metrics['roi_gap']:,.1f}%",
        )

    with c4:
        st.metric(
            "Investment Multiple",
            f"{metrics['investment_multiple']:,.2f}x",
        )

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        st.metric(
            "Capital Required",
            f"?{metrics['capital_required']:,.0f}",
        )

    with c6:
        st.metric(
            "Investor Value",
            f"?{metrics['investor_value']:,.0f}",
        )

    with c7:
        st.metric(
            "Net Investor Gain",
            f"?{metrics['net_gain']:,.0f}",
        )

    with c8:
        st.metric(
            "Decision",
            metrics["decision"],
        )

    if metrics["decision"] == "ATTRACTIVE":
        st.success(
            "Investment economics currently meet or exceed the target."
        )
    elif metrics["decision"] == "BORDERLINE":
        st.warning(
            "Investment economics are close to the target and require review."
        )
    else:
        st.error(
            "Investment economics are currently below the target."
        )

    return metrics
