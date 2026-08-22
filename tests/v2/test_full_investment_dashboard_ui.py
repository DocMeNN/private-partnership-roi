from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.full_investment_dashboard_ui import (
    render_full_investment_dashboard,
)


def test_full_investment_dashboard_import():
    assert callable(render_full_investment_dashboard)
