from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.integrated_investment_view_ui import (
    render_integrated_investment_view,
)


def test_integrated_investment_view_ui_import():
    assert callable(render_integrated_investment_view)
