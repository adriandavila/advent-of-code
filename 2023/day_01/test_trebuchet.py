
from common import get_input_dir
from day_01.part1 import runner as trebuchet_p1
from day_01.part2 import runner as trebuchet_p2

test_dir = get_input_dir(__file__)

def test_trebuchet():
    assert trebuchet_p1(test_dir / "p1sample.txt") == 142

def test_trebuchet_p2():
    assert trebuchet_p2(test_dir / "p2sample.txt") == 281

print(trebuchet_p1(test_dir / "input.txt"))
print(trebuchet_p2(test_dir / "input.txt"))
