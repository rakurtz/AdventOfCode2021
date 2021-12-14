# Advent of Code 2021
# Day 1 - Part I + II

import timeit

with open('inputfiles/day1.txt', "r") as f:
    data = list(map(lambda x: int(x), f.read().splitlines()))


def part1():
    """ first part of puzzle"""
    counter = 0
    for x in range(1, len(data)):
        if data[x] > data[x-1]:
            counter += 1
    return counter


def part2():
    """ second part of puzzle"""
    counter = 0
    for x in range(0, len(data)):
        sum_of_first_three = sum(data[x:x+3])
        sum_of_second_three = sum(data[x+1:x+4])
        if sum_of_second_three > sum_of_first_three:
            counter += 1
    return counter


if __name__ == "__main__":
    start = timeit.default_timer()
    print(part1())
    print(part2())
    stop = timeit.default_timer()

    print(f"\nTook {stop - start} seconds to finish")

    # part 1: 1759 - Took 0.0004945829999999998 seconds to finish
    # part 1: 1805 - Took 0.0008386659999999983 seconds to finish
