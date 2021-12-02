# Advent of Code 2021
# Day 2: Part I + II
import sys
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

    return horizontal * depth


def part1_python3_10():
    """ first part of puzzle"""
    horizontal = 0
    depth = 0

    for line in data:
        instruction, value = line.split()

        match instruction:
            case "forward":
                horizontal += int(value)
            case "down":
                depth += int(value)
            case "up":
                depth -= int(value)

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

    return horizontal * depth


def part2_python3_10():
    """ second part of puzzle"""
    horizontal = 0
    depth = 0
    aim = 0

    for line in data:
        instruction, value = line.split()

        match instruction:
            case "forward":
                horizontal += int(value)
                depth += int(value)*aim
            case "down":
                aim += int(value)
            case "up":
                aim -= int(value)

    return horizontal * depth


if __name__ == "__main__":
    start = timeit.default_timer()
    if int(sys.version[2:4]) < 10:
        print(part1_python3_10())
        print(part2_python3_10())
    else:
        print(part1())
        print(part2())
    stop = timeit.default_timer()

    print(f"\nTook {stop - start} seconds to finish")

    # Part 1 = 2215080 in 0.00020166599999999965 seconds
    # Part 2 = 1864715580 in 0.0002975000000000009 seconds

