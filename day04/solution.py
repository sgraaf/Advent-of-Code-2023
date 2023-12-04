import re
from collections import defaultdict

from aocli import read, to_lines

print("--- Day 4: Scratchcards ---")

# read the input data from `input.txt`
data = {}
for line in to_lines(read("input.txt")):
    # for line in to_lines(read("test_00.txt")):
    # get card number
    if (card_number_m := re.match(r"Card\s+(\d+): ", line)) is not None:
        card_number = int(card_number_m.group(1))

        # split the remaineder of the line into winning numbers and numbers you have
        winning_numbers_s, numbers_you_have_s = line[card_number_m.end() :].split(" | ")

        # split and map to int
        data[card_number] = set(map(int, winning_numbers_s.split())), set(
            map(int, numbers_you_have_s.split())
        )

# part one
print("--- Part One ---")
print(
    sum(
        pow(2, len(set.intersection(*numbers_tup)) - 1)
        if len(set.intersection(*numbers_tup))
        else 0
        for numbers_tup in data.values()
    )
)

# part two
print("--- Part Two ---")
scratchcards_count = defaultdict(int)
for card_number, numbers_tup in data.items():
    scratchcards_count[card_number] += 1
    for next_card_number in range(
        card_number + 1, card_number + 1 + len(set.intersection(*numbers_tup))
    ):
        scratchcards_count[next_card_number] += scratchcards_count[card_number]
print(sum(scratchcards_count.values()))
