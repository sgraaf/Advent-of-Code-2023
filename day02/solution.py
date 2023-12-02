import re
from collections import defaultdict
from functools import reduce
from operator import mul

from aocli import read, to_lines

print("--- Day 2: Cube Conundrum ---")

# read the input data from `input.txt`
data = {}
for line in to_lines(read("input.txt")):
    # for line in to_lines(read("test_00.txt")):
    game_id_m = re.match(r"Game (\d+): ", line)
    if game_id_m is not None:
        game_id = int(game_id_m.group(1))
        game_color_counts = defaultdict(list)

        handfuls = line[game_id_m.end(1) + 2 :].split("; ")
        for handful in handfuls:
            for n, color in re.findall(r"(\d+) ([a-z]+)", handful):
                game_color_counts[color].append(int(n))

        data[game_id] = game_color_counts

# part one
print("--- Part One ---")
color_to_upper_limit_map = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
print(
    sum(
        game_id
        for game_id, color_to_counts_map in data.items()
        if all(
            max(counts) <= color_to_upper_limit_map[color]
            for color, counts in color_to_counts_map.items()
        )
    )
)

# part two
print("--- Part Two ---")
print(
    sum(
        reduce(mul, (max(counts) for counts in color_to_counts_map.values()))
        for color_to_counts_map in data.values()
    )
)
