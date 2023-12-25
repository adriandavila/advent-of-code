from common.utils import get_input_dir

from day_04.part1 import runner as scratchcards_p1
from day_04.part2 import runner as scratchcards_p2

test_dir = get_input_dir(__file__)

def test_scratchcards_part1():
    assert scratchcards_p1(test_dir / "sample.txt") == 13

def test_scratchcards_part2():
    assert scratchcards_p2(test_dir / "sample.txt") == 30

print(scratchcards_p1(test_dir / "input.txt"))
print(scratchcards_p2(test_dir / "input.txt"))
