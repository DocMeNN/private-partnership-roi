import streamlit as st


def render_investment_decision_snapshot(
    scenario,
    totals,
    investor_return_analysis,
    investor_decision_metrics,
    investment_readiness,
):
    st.divider()
    st.header("Investment Decision Snapshot")

    decision = investor_decision_metrics["decision"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Annual Revenue",
            f"₦{scenario['annual_revenue']:,.0f}",
        )

    with c2:
        st.metric(
            "5-Year Revenue",
            f"₦{totals['total_revenue']:,.0f}",
        )

    with c3:
        st.metric(
            "Investor ROI",
            f"{investor_return_analysis.roi_percentage:,.1f}%",
        )

    with c4:
        st.metric(
            "Decision",
            decision,
        )

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        st.metric(
            "Investor Capital",
            f"₦{investor_return_analysis.investor_capital:,.0f}",
        )

    with c6:
        st.metric(
            "Investor Value",
            f"₦{investor_decision_metrics['investor_value']:,.0f}",
        )

    with c7:
        st.metric(
            "Net Investor Gain",
            f"₦{investor_decision_metrics['net_gain']:,.0f}",
        )

    with c8:
        st.metric(
            "Readiness",
            f"{investment_readiness['readiness_percentage']:.0f}%",
        )

    if decision == "ATTRACTIVE":
        st.success(
            "INVESTMENT CASE: ATTRACTIVE"
        )
    elif decision == "BORDERLINE":
        st.warning(
            "INVESTMENT CASE: BORDERLINE"
        )
    else:
        st.error(
            "INVESTMENT CASE: UNATTRACTIVE"
        )

    return {
        "decision": decision,
        "investor_roi": investor_return_analysis.roi_percentage,
        "readiness_percentage": investment_readiness[
            "readiness_percentage"
        ],
    }
