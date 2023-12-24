from common import get_input_dir

from day_02.part1 import runner as cube_conundrum_p1
from day_02.part2 import runner as cube_conundrum_p2

test_dir = get_input_dir(__file__)

def test_cube_conundrum_p1():
    assert cube_conundrum_p1(test_dir / "sample.txt") == 8

def test_cube_conundrum_p2():
    assert cube_conundrum_p2(test_dir / "sample.txt") == 2286

print(cube_conundrum_p1(test_dir / "input.txt"))
print(cube_conundrum_p2(test_dir / "input.txt"))
