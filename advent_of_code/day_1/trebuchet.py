from pathlib import Path
from typing import Literal

def process_line(line: str) -> int:
    calibration_value = 0
    # Find the first number
    for ch in line:
        if ch.isnumeric():
            calibration_value = int(ch) * 10
            break
    # Find the second number
    for ch in reversed(line):
        if ch.isnumeric():
            calibration_value += int(ch)
            break

    return calibration_value



def process_line_v2(line: str) -> int:
    valid_entries: dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }


    calibration_value = 0
    # Find the first number
    char_found = False
    for ch_idx in range(len(line)):
        # Test for a number
        if line[ch_idx].isnumeric():
            calibration_value = int(line[ch_idx]) * 10
            char_found = True

        # Check for all the words
        for i in range(1, min(len(line) - ch_idx, 6)):
            substr = line[ch_idx:ch_idx + i]
            if substr in valid_entries:
                calibration_value = valid_entries[substr] * 10
                char_found = True

        if char_found: break
    
    char_found = False

    # Find the second number
    for ch_idx in range(len(line) - 1, -1, -1):
        # Test for a number
        if line[ch_idx].isnumeric():
            calibration_value += int(line[ch_idx])
            char_found = True

        # Check for all the words
        for i in range(1, min(len(line) - ch_idx + 1, 6)):
            substr = line[ch_idx:ch_idx + i]
            if substr in valid_entries:
                calibration_value += valid_entries[substr]
                char_found = True

        if char_found: break

    return calibration_value

def trebuchet(lines: list[str], version: Literal["v1"] | Literal["v2"] = "v1") -> int:
    acc: int = 0
    for line in lines:
        if version == "v1":
            acc += process_line(line)
        elif version == "v2":
            acc += process_line_v2(line)

    return acc


def runner(input: Path, version: Literal["v1"] | Literal["v2"] = "v1") -> int:
    lines: list[str] = []

    with input.open("r") as file:
        lines = [l.rstrip() for l in file]
    
    return trebuchet(lines, version)
