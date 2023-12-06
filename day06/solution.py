from functools import reduce
from operator import mul

from aocli import read

print("--- Day 6: Wait For It ---")

# read the input data from `input.txt`
data = list(
    zip(*(map(int, line.split()[1:]) for line in read("input.txt").strip().split("\n")))
)
print(data)


def calculate_distance(button_time: int, race_time: int) -> int:
    return (race_time - button_time) * button_time


# part one
print("--- Part One ---")
print(
    reduce(
        mul,
        (
            sum(
                calculate_distance(button_time, race_time) > record_distance
                for button_time in range(race_time + 1)
            )
            for race_time, record_distance in data
        ),
    )
)

# part two
print("--- Part Two ---")
race_time = int("".join((str(race_time) for race_time, _ in data)))
record_distance = int("".join((str(record_distance) for _, record_distance in data)))
print(
    sum(
        calculate_distance(button_time, race_time) > record_distance
        for button_time in range(race_time + 1)
    )
)
