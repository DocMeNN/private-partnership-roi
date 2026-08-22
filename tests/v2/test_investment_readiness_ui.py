from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.investment_readiness_ui import (
    render_investment_readiness_panel,
)


def test_investment_readiness_panel_import():
    assert callable(render_investment_readiness_panel)
