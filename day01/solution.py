import re

from aocli import read, to_lines

print("--- Day 1: Trebuchet?! ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# part one
print("--- Part One ---")
print(
    sum(
        int("".join((re.findall(r"\d", line)[0], re.findall(r"\d", line)[-1])))
        for line in data
    )
)

# part two
print("--- Part Two ---")
str_to_int_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
numbers = []
for line in data:
    digits = re.findall(rf"(?=(\d|{'|'.join(str_to_int_map.keys())}))", line)
    first_digit, last_digit = digits[0], digits[-1]
    first_digit = str_to_int_map.get(first_digit) or int(first_digit)
    last_digit = str_to_int_map.get(last_digit) or int(last_digit)
    numbers.append(first_digit * 10 + last_digit)
print(sum(numbers))
