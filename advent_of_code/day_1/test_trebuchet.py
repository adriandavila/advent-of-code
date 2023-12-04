from trebuchet import runner
from pathlib import Path

test_dir = Path(__file__).parent.resolve()

def test_trebuchet():
    assert runner(test_dir / "sample.txt") == 142
