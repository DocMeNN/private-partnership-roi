import streamlit as st


def render_investment_executive_summary(
    scenario,
    projection,
    investor_return_analysis,
    investor_decision_metrics,
):
    st.divider()
    st.header("Executive Investment Summary")

    st.caption(
        "Integrated V1.2 operating economics with V2 investment economics."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "CHEWs",
            f"{scenario['chews']:,}",
        )

    with c2:
        st.metric(
            "Patients",
            f"{scenario['patients']:,}",
        )

    with c3:
        st.metric(
            "Annual Revenue",
            f"₦{scenario['annual_revenue']:,.0f}",
        )

    with c4:
        st.metric(
            "Annual Contribution",
            f"₦{scenario['annual_contribution']:,.0f}",
        )

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        st.metric(
            "Investor Capital",
            f"₦{investor_return_analysis.investor_capital:,.0f}",
        )

    with c6:
        st.metric(
            "Investor ROI",
            f"{investor_return_analysis.roi_percentage:,.1f}%",
        )

    with c7:
        st.metric(
            "Investment Multiple",
            f"{investor_decision_metrics['investment_multiple']:,.2f}x",
        )

    with c8:
        st.metric(
            "Decision",
            investor_decision_metrics["decision"],
        )

    st.subheader("Five-Year Investment Outlook")

    if projection:
        total_revenue = sum(
            row["annual_revenue"]
            for row in projection
        )
        total_contribution = sum(
            row["annual_contribution"]
            for row in projection
        )

        p1, p2 = st.columns(2)

        with p1:
            st.metric(
                "5-Year Revenue",
                f"₦{total_revenue:,.0f}",
            )

        with p2:
            st.metric(
                "5-Year Contribution",
                f"₦{total_contribution:,.0f}",
            )

    decision = investor_decision_metrics["decision"]

    if decision == "ATTRACTIVE":
        st.success(
            "EXECUTIVE CONCLUSION: The integrated operating and "
            "investment economics currently support an attractive "
            "investment case."
        )
    elif decision == "BORDERLINE":
        st.warning(
            "EXECUTIVE CONCLUSION: The integrated investment case "
            "is borderline and requires commercial review."
        )
    else:
        st.error(
            "EXECUTIVE CONCLUSION: The integrated investment case "
            "is currently below the defined investment threshold."
        )

    return {
        "decision": decision,
        "investor_roi": investor_return_analysis.roi_percentage,
        "investment_multiple": investor_decision_metrics[
            "investment_multiple"
        ],
    }
