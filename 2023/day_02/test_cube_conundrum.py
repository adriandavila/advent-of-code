from cube_conundrum import runner
from pathlib import Path

test_dir = Path(__file__).parent.resolve()

def test_cube_conundrum():
    assert runner(test_dir / "p1sample.txt") == 8

print(runner(test_dir / "input.txt"))