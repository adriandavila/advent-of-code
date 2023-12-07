from gear_ratios import runner, gear_ratios
from pathlib import Path

test_dir = Path(__file__).parent.resolve()

def test_cube_conundrum():
    assert runner(test_dir / "sample.txt") == 4361


def test_manual():
    case_1: list[str] = """
    .............
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_1])) == 0

    ####################################

    case_2: list[str] = """
    .............
    ..*123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_2])) == 123
    
    ####################################

    case_3: list[str] = """
    ..*..........
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_3])) == 123
    
    ####################################

    case_4: list[str] = """
    ...*.........
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_4])) == 123
    
    ####################################

    case_5: list[str] = """
    .............
    ...123.......
    ..*..........
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_5])) == 123

    ####################################

    case_6: list[str] = """
    .............
    ...123.......
    ...*.........
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_6])) == 123

    ####################################

    case_7: list[str] = """
    .............
    ...123.......
    ......*......
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_7])) == 123

    ####################################

    case_8: list[str] = """
    .............
    ...123*......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_8])) == 123

    ####################################

    case_9: list[str] = """
    ......*......
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_9])) == 123

    ####################################

    case_10: list[str] = """
    .....*.......
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_9])) == 123

def test_edge():
    case_1: list[str] = """
    .....
    12*..
    .....
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_1])) == 12

    ####################################

    case_1: list[str] = """
    ..*..
    12...
    .....
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_1])) == 12

    ####################################

    case_3: list[str] = """
    .....
    .....
    ..*12
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_3])) == 12

    ####################################

    case_4: list[str] = """
    .....
    ..*..
    ...12
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_4])) == 12

    ####################################

    case_5: list[str] = """
    .....
    ...*.
    ...12
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_5])) == 12

    ####################################

    case_5: list[str] = """
    .....
    .*...
    ...12
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_5])) == 0

    ####################################

def test_too_far():
    case_1: list[str] = """
    .............
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_1])) == 0

    ####################################

    case_2: list[str] = """
    .............
    .*.123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_2])) == 0
    
    ####################################

    case_3: list[str] = """
    .*...........
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_3])) == 0
    
    ####################################

    case_4: list[str] = """
    ...*.........
    .............
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_4])) == 0
    
    ####################################

    case_5: list[str] = """
    .............
    ...123.......
    .*...........
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_5])) == 0

    ####################################

    case_6: list[str] = """
    .............
    ...123.......
    .............
    ...*.........
    """.strip().split("\n")
    
    assert(gear_ratios([_.strip() for _ in case_6])) == 0

    ####################################

    case_7: list[str] = """
    .............
    ...123.......
    .......*.....
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_7])) == 0

    ####################################

    case_8: list[str] = """
    .............
    ...123.*.....
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_8])) == 0

    ####################################

    case_9: list[str] = """
    .......*.....
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_9])) == 0

    ####################################

    case_10: list[str] = """
    .....*.......
    .............
    ...123.......
    .............
    """.strip().split("\n")

    assert(gear_ratios([_.strip() for _ in case_9])) == 0

def test_gear_ratio_part_2():
    assert runner(test_dir / "sample.txt") == 467835

print(runner(test_dir / "input.txt"))