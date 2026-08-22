from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_v12_v2_full_dashboard_integration_imports():
    from dashboard.v2.full_investment_dashboard_ui import (
        render_full_investment_dashboard,
    )
    from dashboard.v2.v1_v2_summary_ui import (
        render_v1_v2_summary,
    )
    from dashboard.v2.investment_executive_summary_ui import (
        render_investment_executive_summary,
    )
    from dashboard.v2.investment_readiness_ui import (
        render_investment_readiness,
    )
    from dashboard.v2.investment_decision_snapshot_ui import (
        render_investment_decision_snapshot,
    )
    from dashboard.v2.v12_v2_integration_status_ui import (
        render_v12_v2_integration_status,
    )

    assert callable(render_full_investment_dashboard)
    assert callable(render_v1_v2_summary)
    assert callable(render_investment_executive_summary)
    assert callable(render_investment_readiness)
    assert callable(render_investment_decision_snapshot)
    assert callable(render_v12_v2_integration_status)
