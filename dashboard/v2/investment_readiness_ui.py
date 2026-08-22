import streamlit as st


def render_investment_readiness_panel(
    investor_decision_metrics,
    investment_assumptions,
):
    st.divider()
    st.header("Investment Readiness")

    decision = investor_decision_metrics["decision"]
    roi = investor_decision_metrics["investor_roi"]
    target = investor_decision_metrics["target_roi"]
    multiple = investor_decision_metrics["investment_multiple"]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Current ROI",
            f"{roi:,.1f}%",
        )

    with c2:
        st.metric(
            "Target ROI",
            f"{target:,.1f}%",
        )

    with c3:
        st.metric(
            "Investment Multiple",
            f"{multiple:,.2f}x",
        )

    st.subheader("Readiness Assessment")

    readiness_items = [
        (
            "Investor Capital",
            investment_assumptions.investor_capital > 0,
        ),
        (
            "Investment Period",
            investment_assumptions.investment_period_years > 0,
        ),
        (
            "Ownership Structure",
            0 < investment_assumptions.ownership_percentage <= 100,
        ),
        (
            "Exit Multiple",
            investment_assumptions.exit_multiple > 0,
        ),
        (
            "Investor ROI Target",
            investment_assumptions.investor_return_target > 0,
        ),
    ]

    completed = sum(
        1
        for _, passed in readiness_items
        if passed
    )
    total = len(readiness_items)
    readiness_percentage = (
        completed / total * 100
        if total
        else 0
    )

    st.progress(
        readiness_percentage / 100,
        text=(
            f"Investment readiness: "
            f"{completed}/{total} criteria satisfied "
            f"({readiness_percentage:.0f}%)"
        ),
    )

    for label, passed in readiness_items:
        if passed:
            st.success(f"{label}: READY")
        else:
            st.error(f"{label}: REVIEW REQUIRED")

    if decision == "ATTRACTIVE" and readiness_percentage == 100:
        st.success(
            "READY FOR INVESTMENT DISCUSSION: "
            "Core investment assumptions are complete and "
            "the current economics meet the target."
        )
    elif decision == "BORDERLINE":
        st.warning(
            "INVESTMENT REVIEW REQUIRED: "
            "The economics are borderline against the target."
        )
    else:
        st.warning(
            "INVESTMENT READINESS NOT CONFIRMED: "
            "Review the economics and outstanding assumptions."
        )

    return {
        "decision": decision,
        "readiness_percentage": readiness_percentage,
        "criteria_completed": completed,
        "criteria_total": total,
    }
