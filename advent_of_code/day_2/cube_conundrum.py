from pathlib import Path
from typing import Literal

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def cube_conundrum(games: list[int, list[list[tuple[int, Literal["blue"] | Literal["red"] | Literal["green"]]]]]) -> int:
    def is_valid_game(game: list[list[tuple[int, Literal["blue"] | Literal["red"] | Literal["green"]]]]) -> bool:
        for batch in game:
            blue_drawn = sum([d[0] for d in batch if d[1] == "blue"])
            if blue_drawn > MAX_BLUE:
                return False

            red_drawn = sum([d[0] for d in batch if d[1] == "red"])
            if red_drawn > MAX_RED:
                return False
            
            green_drawn = sum([d[0] for d in batch if d[1] == "green"])
            if green_drawn > MAX_GREEN:
                return False
        
        return True

    return sum([g[0] for g in games if is_valid_game(g[1])])


def runner(input: Path) -> int:
    games: list[int, list[list[tuple[int, Literal["blue"] | Literal["red"] | Literal["green"]]]]] = []

    with input.open("r") as file:
        for line in file:
            [game_title, game_info] = line.strip().split(":")

            # Get the game ID
            game_id = int(game_title.split(" ")[1].strip())

            # Parse the draws
            draws = game_info.split(";")
            draws = [draw.strip().split(",") for draw in draws]

            for i in range(len(draws)):
                draws[i] = [entry.strip().split(" ") for entry in draws[i]]
                draws[i] = [(int(d[0]), d[1]) for d in draws[i]]
            
            games.append([game_id, draws])
    
    return cube_conundrum(games)
