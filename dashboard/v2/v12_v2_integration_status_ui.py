import streamlit as st


def render_v12_v2_integration_status(
    scenario,
    projection,
    investor_return_analysis,
    investor_decision_metrics,
    investment_readiness,
):
    st.divider()
    st.header("V1.2 + V2 Integration Status")

    checks = {
        "V1.2 Operating Model": scenario is not None,
        "Five-Year Projection": bool(projection),
        "Investor Return Analysis": investor_return_analysis is not None,
        "Investor Decision Metrics": investor_decision_metrics is not None,
        "Investment Readiness": investment_readiness is not None,
    }

    completed = sum(checks.values())
    total = len(checks)
    percentage = completed / total * 100 if total else 0

    st.progress(
        percentage / 100,
        text=f"Integration completeness: {completed}/{total} ({percentage:.0f}%)",
    )

    for label, passed in checks.items():
        if passed:
            st.success(f"{label}: INTEGRATED")
        else:
            st.warning(f"{label}: PENDING")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Integration Status",
            "COMPLETE" if completed == total else "IN PROGRESS",
        )

    with c2:
        st.metric(
            "Investor Decision",
            investor_decision_metrics["decision"],
        )

    with c3:
        st.metric(
            "Readiness",
            f"{investment_readiness['readiness_percentage']:.0f}%",
        )

    if completed == total:
        st.success(
            "V1.2 and V2 are fully connected into one integrated "
            "operating and investment decision framework."
        )

    return {
        "completed": completed,
        "total": total,
        "percentage": percentage,
        "status": "COMPLETE" if completed == total else "IN PROGRESS",
    }
