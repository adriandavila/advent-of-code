from pathlib import Path
from dataclasses import dataclass

@dataclass
class Scratchcard:
    winning_numbers: set[int]
    card_numbers: list[int]

def scratchcards(scratchcards: list[Scratchcard]) -> int:
    score: int = 0

    for card in scratchcards:
        card_result: int = 0
        for n in card.card_numbers:
            if n in card.winning_numbers:
                card_result = card_result * 2 if card_result > 0 else 1
        
        score += card_result
    
    return score


def runner(input: Path) -> int:
    collected_cards: list[Scratchcard] = []

    with input.open("r") as file:
        for line in file:
            [_, card_data] = line.split(":")
            card_data = card_data.strip()

            [raw_winning_numbers, raw_card_numbers] = card_data.split("|")
            raw_winning_numbers = raw_winning_numbers.strip()
            raw_card_numbers = raw_card_numbers.strip()

            winning_numbers = set([int(n.strip()) for n in raw_winning_numbers.split()])
            card_numbers = [int(n.strip()) for n in raw_card_numbers.split()]

            card = Scratchcard(
                winning_numbers=winning_numbers,
                card_numbers=card_numbers
            )

            collected_cards.append(card)
    
    return scratchcards(collected_cards)