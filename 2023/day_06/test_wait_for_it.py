from common.utils import get_input_dir

from day_06.part1 import runner as wait_for_it_p1

# from day_06.part2 import runner as wait_for_it_p2

test_dir = get_input_dir(__file__)


def test_seed_fertilizer_p1():
    assert wait_for_it_p1(test_dir / "sample.txt") == 288


# def test_seed_fertilizer_p2():
#     assert wait_for_it_p2(test_dir / "sample.txt") == 46


print(wait_for_it_p1(test_dir / "input.txt"))
# print(wait_for_it_p2(test_dir / "input.txt"))
