from trebuchet import runner
from pathlib import Path

test_dir = Path(__file__).parent.resolve()

def test_trebuchet():
    assert runner(test_dir / "p1sample.txt") == 142

def test_trebuchet_vs():
    assert runner(test_dir / "p2sample.txt", "v2") == 281

print(runner(test_dir / "input.txt", "v1"))