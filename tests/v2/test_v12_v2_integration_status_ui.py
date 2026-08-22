from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.v12_v2_integration_status_ui import (
    render_v12_v2_integration_status,
)


def test_v12_v2_integration_status_import():
    assert callable(render_v12_v2_integration_status)
