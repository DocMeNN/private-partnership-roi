import streamlit as st


def render_integrated_investment_view(
    integrated_view,
):
    st.divider()
    st.header("V2 - Integrated Investment View")

    st.subheader(
        f"Operating Scale - {integrated_view.chews:,} CHEWs"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("CHEWs", f"{integrated_view.chews:,}")

    with c2:
        st.metric("Patients", f"{integrated_view.patients:,}")

    with c3:
        st.metric(
            "Annual Revenue",
            f"NGN {integrated_view.annual_revenue:,.0f}",
        )

    with c4:
        st.metric(
            "Annual CHEW Cost",
            f"NGN {integrated_view.annual_chew_cost:,.0f}",
        )

    st.subheader("Operating Economics")

    c5, c6, c7 = st.columns(3)

    with c5:
        st.metric(
            "Setup Cost",
            f"NGN {integrated_view.setup_cost:,.0f}",
        )

    with c6:
        st.metric(
            "Annual Contribution",
            f"NGN {integrated_view.annual_contribution:,.0f}",
        )

    with c7:
        st.metric(
            "Investor Capital",
            f"NGN {integrated_view.investor_capital:,.0f}",
        )

    st.subheader("Investor Economics")

    c8, c9, c10, c11 = st.columns(4)

    with c8:
        st.metric(
            "Investor Value",
            f"NGN {integrated_view.investor_value:,.0f}",
        )

    with c9:
        st.metric(
            "Net Investor Gain",
            f"NGN {integrated_view.investor_gain:,.0f}",
        )

    with c10:
        st.metric(
            "Investor ROI",
            f"{integrated_view.investor_roi:,.1f}%",
        )

    with c11:
        st.metric(
            "Investment Multiple",
            f"{integrated_view.investment_multiple:,.2f}x",
        )

    st.subheader("Investment Decision")

    c12, c13, c14 = st.columns(3)

    with c12:
        st.metric(
            "Target ROI",
            f"{integrated_view.target_roi:,.1f}%",
        )

    with c13:
        st.metric(
            "ROI Gap",
            f"{integrated_view.roi_gap:,.1f}%",
        )

    with c14:
        st.metric(
            "Decision",
            integrated_view.decision,
        )

    if integrated_view.decision == "ATTRACTIVE":
        st.success(
            "Integrated investment economics are currently attractive."
        )
    elif integrated_view.decision == "BORDERLINE":
        st.warning(
            "Integrated investment economics require review."
        )
    else:
        st.error(
            "Integrated investment economics are currently unattractive."
        )

    return integrated_view
