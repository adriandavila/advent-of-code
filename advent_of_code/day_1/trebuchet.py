from pathlib import Path

def trebuchet(lines: list[str]) -> int:
    def process_line(line: str) -> int:
        # Find first char
        calibration_value = 0
        for ch in line:
            if ch.isnumeric():
                calibration_value = int(ch) * 10
                break
        
        for ch in reversed(line):
            if ch.isnumeric():
                calibration_value += int(ch)
                break

        return calibration_value

    acc: int = 0

    for line in lines:
        acc += process_line(line)

    return acc


def runner(input: Path) -> int:
    lines: list[str] = []

    with input.open("r") as file:
        lines = [l.rstrip() for l in file]
    
    return trebuchet(lines)
