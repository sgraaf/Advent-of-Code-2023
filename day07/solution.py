from __future__ import annotations

from collections import Counter
from enum import IntEnum

from aocli import read, to_lines

print("--- Day 7: Camel Cards ---")

# read the input data from `input.txt`
data = [
    (tuple(int(c) if c.isdigit() else c for c in line.split()[0]), int(line.split()[1]))
    for line in to_lines(read("input.txt"))
]
print(data)


class CamelCardsType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


CARDS = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]


def determine_hand_type(  # noqa: PLR0911
    hand: tuple[str | int, ...], joker: str | int | None = None
) -> CamelCardsType:
    if joker is not None:
        for most_common_card, _ in Counter(hand).most_common():
            if most_common_card != joker:
                hand = tuple(
                    most_common_card if card == joker else card for card in hand
                )
                break
        else:
            hand = ("A",) * 5

    card_counts = tuple(count for _, count in Counter(hand).most_common())

    if card_counts == (5,):  # five of a kind
        return CamelCardsType.FIVE_OF_A_KIND
    if card_counts == (4, 1):  # four of a kind
        return CamelCardsType.FOUR_OF_A_KIND
    if card_counts == (3, 2):  # full house
        return CamelCardsType.FULL_HOUSE
    if card_counts == (3, 1, 1):  # three of a kind
        return CamelCardsType.THREE_OF_A_KIND
    if card_counts == (2, 2, 1):  # two pair
        return CamelCardsType.TWO_PAIR
    if card_counts == (2, 1, 1, 1):  # one pair
        return CamelCardsType.ONE_PAIR

    return CamelCardsType.HIGH_CARD


def determine_sort_key(
    hand: tuple[str | int, ...], joker: str | int | None = None
) -> tuple[int, tuple[int, int, int, int, int]]:
    return determine_hand_type(hand, joker=joker), tuple(
        CARDS.index(card) for card in hand
    )


# part one
print("--- Part One ---")
print(
    sum(
        bet * rank
        for rank, (hand, bet) in enumerate(
            sorted(data, key=lambda x: determine_sort_key(x[0])), start=1
        )
    )
)

# part two
print("--- Part Two ---")
JOKER = "J"
CARDS.remove(JOKER)
CARDS.insert(0, JOKER)
print(
    sum(
        bet * rank
        for rank, (hand, bet) in enumerate(
            sorted(data, key=lambda x: determine_sort_key(x[0], joker="J")), start=1
        )
    )
)
