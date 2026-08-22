from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.v1_v2_summary_ui import (
    render_v1_v2_summary,
)


def test_v1_v2_summary_ui_import():
    assert callable(render_v1_v2_summary)
