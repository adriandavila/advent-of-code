from pathlib import Path

def get_test_dir(file: str) -> Path:
    day, year = Path(file).parent.name, Path(file).parent.parent.name
    return Path(__file__).parent.parent / "aoc-inputs" / year / day
