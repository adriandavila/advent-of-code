from pathlib import Path
from dataclasses import dataclass

@dataclass
class Scratchcard:
    winning_numbers: set[int]
    card_numbers: list[int]

def scratchcards(scratchcards: list[Scratchcard]) -> int:
    num_cards = [1] * len(scratchcards)

    for i, card in enumerate(scratchcards):
        matching_numbers = sum([1 for n in card.card_numbers if n in card.winning_numbers])
        for card_idx in range(i + 1, i + 1 + matching_numbers):
            num_cards[card_idx] += num_cards[i]


    return sum(num_cards)


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
