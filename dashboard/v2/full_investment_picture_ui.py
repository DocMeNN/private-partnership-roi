import streamlit as st

from dashboard.v2.v1_v2_summary_ui import (
    render_v1_v2_summary,
)


def render_full_investment_picture(
    scenario,
    integrated_view,
):
    st.divider()
    st.header("V1.2 + V2 - Full Investment Picture")

    render_v1_v2_summary(
        scenario=scenario,
        integrated_view=integrated_view,
    )

    st.subheader("Executive Investment Readout")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Operating Contribution",
            f"NGN {integrated_view.annual_contribution:,.0f}",
        )

    with c2:
        st.metric(
            "Investor Net Gain",
            f"NGN {integrated_view.net_investor_gain:,.0f}",
        )

    with c3:
        st.metric(
            "Investment Decision",
            integrated_view.decision,
        )

    if integrated_view.decision == "ATTRACTIVE":
        st.success(
            "V1.2 operating economics and V2 investor economics "
            "currently support an attractive investment case."
        )
    elif integrated_view.decision == "BORDERLINE":
        st.warning(
            "The combined investment case is borderline and "
            "requires commercial review before commitment."
        )
    else:
        st.error(
            "The combined investment case is currently below "
            "the defined investment threshold."
        )

    return integrated_view
