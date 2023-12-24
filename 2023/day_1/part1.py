from pathlib import Path

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


def trebuchet(lines: list[str]) -> int:
    acc: int = 0
    for line in lines:
        acc += process_line(line)
        
    return acc


def runner(input: Path) -> int:
    lines: list[str] = []

    with input.open("r") as file:
        lines = [l.rstrip() for l in file]
    
    return trebuchet(lines)
