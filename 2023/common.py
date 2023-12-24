from pathlib import Path

def getTestDir(file: str) -> Path:
    day, year = Path(file).parent.name, Path(file).parent.parent.name
    return Path(__file__).parent / "aoc-inputs" / year / day