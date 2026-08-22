import streamlit as st


def render_v1_v2_summary(
    scenario,
    integrated_view,
):
    st.divider()
    st.header("V1.2 + V2 - Full Investment Picture")

    st.subheader("Operating Scale")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "CHEWs",
            f"{integrated_view.chews:,}",
        )

    with c2:
        st.metric(
            "Patients",
            f"{integrated_view.patients:,}",
        )

    with c3:
        st.metric(
            "Monthly Revenue",
            f"NGN {scenario['monthly_revenue']:,.0f}",
        )

    with c4:
        st.metric(
            "Annual Revenue",
            f"NGN {integrated_view.annual_revenue:,.0f}",
        )

    st.subheader("V1.2 Operating Economics")

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        st.metric(
            "Monthly CHEW Cost",
            f"NGN {scenario['monthly_chew_cost']:,.0f}",
        )

    with c6:
        st.metric(
            "Monthly Contribution",
            f"NGN {scenario['monthly_contribution']:,.0f}",
        )

    with c7:
        st.metric(
            "Setup Cost",
            f"NGN {scenario['confirmed_setup_cost']:,.0f}",
        )

    with c8:
        st.metric(
            "Annual Contribution",
            f"NGN {integrated_view.annual_contribution:,.0f}",
        )

    st.subheader("V2 Investor Economics")

    c9, c10, c11, c12 = st.columns(4)

    with c9:
        st.metric(
            "Investor Capital",
            f"NGN {integrated_view.investor_capital:,.0f}",
        )

    with c10:
        st.metric(
            "Investor Value",
            f"NGN {integrated_view.investor_value:,.0f}",
        )

    with c11:
        st.metric(
            "Investor ROI",
            f"{integrated_view.investor_roi:,.1f}%",
        )

    with c12:
        st.metric(
            "Investment Multiple",
            f"{integrated_view.investment_multiple:,.2f}x",
        )

    st.subheader("Investment Decision")

    c13, c14, c15 = st.columns(3)

    with c13:
        st.metric(
            "Target ROI",
            f"{integrated_view.target_roi:,.1f}%",
        )

    with c14:
        st.metric(
            "ROI Gap",
            f"{integrated_view.roi_gap:,.1f}%",
        )

    with c15:
        st.metric(
            "Decision",
            integrated_view.decision,
        )

    if integrated_view.decision == "ATTRACTIVE":
        st.success(
            "The combined V1.2 operating model and V2 investor economics are currently attractive."
        )
    elif integrated_view.decision == "BORDERLINE":
        st.warning(
            "The combined investment picture requires commercial review."
        )
    else:
        st.error(
            "The combined investment picture is currently unattractive."
        )

    return integrated_view
