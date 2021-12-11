# Advent of Code 2021
# Day 7: Part I

import timeit
from statistics import median


def calculate_fuel_for_point(horizontal_positions: list, reference_position: int):
    fuel = 0
    for crab in horizontal_positions:
        fuel += abs(crab - reference_position)
    return fuel


def calculate_lowest_fuel(horizontal_positions: list):
    """ Numeric solution of finding the median, returns a tuple of fuel used for optimal position """
    """ not used in this program """

    fuels = []
    for position in range(min(horizontal_positions), max(horizontal_positions)):
        fuels.append((calculate_fuel_for_point(horizontal_positions, position), position))

    return min(fuels)


if __name__ == "__main__":
    start = timeit.default_timer()

    with open('inputfiles/day7.txt', "r") as f:
        horizontal_positions = list(map(lambda x: int(x), f.read().split(",")))

    print(f"Solution Part I: {calculate_fuel_for_point(horizontal_positions, median(horizontal_positions))}")

    stop = timeit.default_timer()

    print(f"Took {stop - start} seconds to finish\n")



