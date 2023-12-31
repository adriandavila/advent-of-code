from pathlib import Path
from collections import namedtuple

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
    
    return acc


def runner(input: Path) -> int:
    schematic_lines: list[str] = []

    with input.open("r") as file:
        schematic_lines = [_.strip() for _ in file.readlines()]
    
    return gear_ratios(schematic_lines)
