# Advent of Code 2021
# Day 2: Part I + II

import timeit

with open('inputfiles/day2.txt', "r") as f:
    data = f.read().splitlines()


def part1():
    """ first part of puzzle"""
    horizontal = 0
    depth = 0

    for line in data:
        instruction, value = line.split()

        if instruction == "forward":
            horizontal += int(value)
        elif instruction == "down":
            depth += int(value)
        elif instruction == "up":
            depth -= int(value)
        else:
            print("Error reading the instructions")

    return horizontal * depth


def part2():
    """ second part of puzzle"""
    horizontal = 0
    depth = 0
    aim = 0

    for line in data:
        instruction, value = line.split()

        if instruction == "forward":
            horizontal += int(value)
            depth += int(value)*aim
        elif instruction == "down":
            aim += int(value)
        elif instruction == "up":
            aim -= int(value)
        else:
            print("Error reading the instructions")

    return horizontal * depth


if __name__ == "__main__":
    start = timeit.default_timer()
    print(part1())
    print(part2())
    stop = timeit.default_timer()

    print(f"\nTook {stop - start} seconds to finish")

    # Part 1 = 2215080 in 0.00020166599999999965 seconds
    # Part 2 = 1864715580 in 0.0002975000000000009 seconds

