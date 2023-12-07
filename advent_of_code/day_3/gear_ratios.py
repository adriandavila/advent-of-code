from pathlib import Path
from collections import namedtuple
from math import prod

SchematicNumber = namedtuple("SchematicNumber", ["line_idx", "start_idx", "end_idx"])

def gear_ratios(schematic: list[str]) -> int:

    number_indexes: list[SchematicNumber] = []

    # identify numbers in the schematic
    for line_idx, line in enumerate(schematic):
        l, r = 0, 0
        while r < len(line):
            if line[r].isnumeric():
                r += 1
            else:
                if l != r:
                    number_indexes.append(SchematicNumber(line_idx, l, r))
                
                l = r = r + 1
        
        if l < r:
            number_indexes.append(SchematicNumber(line_idx, l, r))
    
    with open("temporary_result.txt", "w") as f:
        for num in number_indexes:
            f.write(schematic[num.line_idx][num.start_idx:num.end_idx] + "\n")

    # decide if numbers are adjacent to a symbol and add them to tally
    def is_in_range(x: int, y: int) -> bool:
        return 0 <= x < len(schematic[0]) and 0 <= y < len(schematic)
    
    acc: int = 0

    def is_adjacent_to_symbol(num: SchematicNumber) -> bool:
        nonlocal schematic

        # Check above
        for x in range(num.start_idx - 1, num.end_idx + 1):
            if is_in_range(x, num.line_idx - 1):
                ch = schematic[num.line_idx - 1][x]
                if ch != "." and not ch.isnumeric():
                    return True

        # Check below
        for x in range(num.start_idx - 1, num.end_idx + 1):
            if is_in_range(x, num.line_idx + 1):
                ch = schematic[num.line_idx + 1][x]
                if ch != "." and not ch.isnumeric():
                    return True

        # Check left
        if is_in_range(num.start_idx - 1, num.line_idx):
            ch: chr = schematic[num.line_idx][num.start_idx - 1]
            if ch != "." and not ch.isnumeric():
                return True

        # Check right
        if is_in_range(num.end_idx, num.line_idx):
            ch = schematic[num.line_idx][num.end_idx] 
            if ch != "." and not ch.isnumeric():
                return True
        
        return False
    
    for num in number_indexes:
        if is_adjacent_to_symbol(num):
            acc += int(schematic[num.line_idx][num.start_idx:num.end_idx])

    """
    # PART 2 SOLUTION
    cache = [[(0, []) for _ in range(len(schematic[0]))] for _ in range(len(schematic))]

    def adjacent_symbol(num: SchematicNumber) -> tuple[int] | None:
        nonlocal schematic

        # Check above
        for x in range(num.start_idx - 1, num.end_idx + 1):
            if is_in_range(x, num.line_idx - 1):
                ch = schematic[num.line_idx - 1][x]
                if ch == "*":
                    return (x, num.line_idx - 1)

        # Check below
        for x in range(num.start_idx - 1, num.end_idx + 1):
            if is_in_range(x, num.line_idx + 1):
                ch = schematic[num.line_idx + 1][x]
                if ch == "*":
                    return (x, num.line_idx + 1)

        # Check left
        if is_in_range(num.start_idx - 1, num.line_idx):
            ch: chr = schematic[num.line_idx][num.start_idx - 1]
            if ch == "*":
                return (num.start_idx - 1, num.line_idx) 

        # Check right
        if is_in_range(num.end_idx, num.line_idx):
            ch = schematic[num.line_idx][num.end_idx] 
            if ch == "*":
                return (num.end_idx , num.line_idx)
        
        return None
    
    for num in number_indexes:
        if adjacent_symbol(num) is not None:
            x, y = adjacent_symbol(num)
            cache[y][x] = (cache[y][x][0] + 1, cache[y][x][1] + [int(schematic[num.line_idx][num.start_idx:num.end_idx])])

    partial_sum: int = 0
    for y in range(len(cache)):
        for x in range(len(cache[0])):
            if cache[y][x][0] == 2:
                partial_sum += prod(cache[y][x][1])

        
    return partial_sum
    """




def runner(input: Path) -> int:
    schematic_lines: list[str] = []

    with input.open("r") as file:
        schematic_lines = [_.strip() for _ in file.readlines()]
    
    return gear_ratios(schematic_lines)
