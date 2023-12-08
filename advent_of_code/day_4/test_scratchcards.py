from scratchcards import runner
from pathlib import Path

test_dir = Path(__file__).parent.resolve()

# def test_scratchcards():
#     assert runner(test_dir / "sample.txt") == 13
def test_scratchcards_part2():
    assert runner(test_dir / "sample.txt") == 30

print(runner(test_dir / "input.txt"))
