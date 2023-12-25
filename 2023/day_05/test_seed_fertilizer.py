from common.utils import get_input_dir

from day_05.part1 import runner as seed_fertilizer_p1
from day_05.part2 import runner as seed_fertilizer_p2

test_dir = get_input_dir(__file__)


def test_seed_fertilizer_p1():
    assert seed_fertilizer_p1(test_dir / "sample.txt") == 35


def test_seed_fertilizer_p2():
    assert seed_fertilizer_p2(test_dir / "sample.txt") == 46


print(seed_fertilizer_p1(test_dir / "input.txt"))
print(seed_fertilizer_p2(test_dir / "input.txt"))
