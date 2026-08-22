from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.integrated_investment_view import (
    build_integrated_investment_view,
)


def test_integrated_investment_view():
    scenario = {
        "chews": 100,
        "patients": 1000,
        "monthly_revenue": 7_500_000,
        "annual_revenue": 90_000_000,
        "monthly_chew_cost": 11_000_000,
        "confirmed_setup_cost": 10_000_000,
        "monthly_contribution": -3_500_000,
    }

    projection_totals = {
        "investor_capital": 50_000_000,
    }

    class ReturnAnalysis:
        total_investor_value = 98_000_000
        net_investor_gain = 48_000_000

    decision_metrics = {
        "investor_roi": 96.0,
        "target_roi": 20.0,
        "roi_gap": 76.0,
        "investment_multiple": 1.96,
        "decision": "ATTRACTIVE",
    }

    result = build_integrated_investment_view(
        scenario=scenario,
        projection_totals=projection_totals,
        investor_return_analysis=ReturnAnalysis(),
        investor_decision_metrics=decision_metrics,
    )

    assert result.chews == 100
    assert result.patients == 1000
    assert result.annual_revenue == 90_000_000
    assert result.annual_chew_cost == 132_000_000
    assert result.annual_contribution == -42_000_000
    assert result.investor_capital == 50_000_000
    assert result.investor_value == 98_000_000
    assert result.investor_gain == 48_000_000
    assert result.investor_roi == 96.0
    assert result.target_roi == 20.0
    assert result.roi_gap == 76.0
    assert result.investment_multiple == 1.96
    assert result.decision == "ATTRACTIVE"
