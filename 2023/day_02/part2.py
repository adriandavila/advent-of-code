from pathlib import Path
from typing import Literal

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def cube_conundrum_power(games: list[int, list[list[tuple[int, Literal["blue"] | Literal["red"] | Literal["green"]]]]]) -> int:
    def game_power(game: list[list[tuple[int, Literal["blue"] | Literal["red"] | Literal["green"]]]]) -> bool:
        min_blue = 0
        min_red = 0
        min_green = 0

        for batch in game:
            blue_drawn = sum([d[0] for d in batch if d[1] == "blue"])
            min_blue = max(min_blue, blue_drawn)

            red_drawn = sum([d[0] for d in batch if d[1] == "red"])
            min_red = max(min_red, red_drawn)
            
            green_drawn = sum([d[0] for d in batch if d[1] == "green"])
            min_green = max(min_green, green_drawn)
        
        return min_blue * min_red * min_green

    return sum([game_power(g[1]) for g in games])


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
    
    return cube_conundrum_power(games)
