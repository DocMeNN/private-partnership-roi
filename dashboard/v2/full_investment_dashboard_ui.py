import streamlit as st


def render_full_investment_dashboard(
    scenario,
    totals,
    projection,
    investor_return_analysis,
    investor_decision_metrics,
    investment_readiness,
    integration_status,
    decision_snapshot,
):
    st.divider()
    st.header("FULL INVESTMENT DASHBOARD")

    st.caption(
        "V1.2 operating economics + V2 investment economics + "
        "decision readiness."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Operating Scale",
            f"{scenario['chews']:,} CHEWs",
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
            "5-Year Revenue",
            f"₦{totals['total_revenue']:,.0f}",
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
            "Investor Multiple",
            f"{investor_decision_metrics['investment_multiple']:,.2f}x",
        )

    with c8:
        st.metric(
            "Decision",
            investor_decision_metrics["decision"],
        )

    st.subheader("Five-Year Projection")

    if projection:
        rows = []

        for row in projection:
            rows.append(
                {
                    "Year": row.get("year"),
                    "CHEWs": row.get("chews"),
                    "Patients": row.get("patients"),
                    "Revenue": row.get("annual_revenue"),
                    "Contribution": row.get("annual_contribution"),
                }
            )

        if rows:
            st.dataframe(
                rows,
                use_container_width=True,
            )

    st.subheader("Investment Readiness")

    st.progress(
        investment_readiness["readiness_percentage"] / 100,
        text=(
            f"{investment_readiness['criteria_completed']}/"
            f"{investment_readiness['criteria_total']} "
            "readiness criteria satisfied"
        ),
    )

    st.subheader("Integration Status")

    st.metric(
        "V1.2 + V2 Integration",
        integration_status["status"],
    )

    st.metric(
        "Integration Completeness",
        f"{integration_status['percentage']:.0f}%",
    )

    st.subheader("Executive Decision")

    decision = decision_snapshot["decision"]

    if decision == "ATTRACTIVE":
        st.success(
            "ATTRACTIVE — the current operating and investment "
            "economics support proceeding to investment discussion."
        )
    elif decision == "BORDERLINE":
        st.warning(
            "BORDERLINE — the investment case requires commercial "
            "and financial review."
        )
    else:
        st.error(
            "UNATTRACTIVE — the current investment economics do "
            "not meet the required threshold."
        )

    return {
        "decision": decision,
        "integration_status": integration_status["status"],
        "readiness_percentage": investment_readiness[
            "readiness_percentage"
        ],
        "investor_roi": investor_return_analysis.roi_percentage,
        "investment_multiple": investor_decision_metrics[
            "investment_multiple"
        ],
    }
