from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dashboard.v2.investor_return_analysis import (
    calculate_investor_return,
)


def test_investor_return_analysis():

    result = calculate_investor_return(
        investor_capital=50_000_000,
        total_contribution=240_000_000,
        investor_return_target=0.20,
        ownership_percentage=20.0,
        exit_multiple=1.0,
    )

    assert result.target_return == 10_000_000
    assert result.investor_share_of_contribution == 48_000_000
    assert result.exit_value == 50_000_000
    assert result.total_investor_value == 98_000_000
    assert result.net_investor_gain == 48_000_000
    assert result.roi_percentage == 96.0
