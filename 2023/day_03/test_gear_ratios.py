from common import get_test_dir

from day_03.part1 import runner as gear_ratio_p1
from day_03.part2 import runner as gear_ratio_p2

test_dir = get_test_dir(__file__)

def test_gear_ratio_p1():
    assert gear_ratio_p1(test_dir / "sample.txt") == 4361

def test_gear_ratio_part_2():
    assert gear_ratio_p2(test_dir / "sample.txt") == 467835

print(gear_ratio_p1(test_dir / "input.txt"))
print(gear_ratio_p2(test_dir / "input.txt"))
