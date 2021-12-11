# Advent of Code 2021
# Day 7: Part I

import timeit
from statistics import median


def calculate_fuel_for_point(horizontal_positions: list, reference_position: int, mod_increase=False):
    """ calculates and returnes burned fuel for all crabs moving to reference point """
    """ with mod_increase=True it uses calculation for Part II of puzzle"""

    fuel = 0
    for crab in horizontal_positions:
        if not mod_increase:
            fuel += abs(crab - reference_position)
        else:
            # using Gauß's formula for Part II
            n = abs(crab - reference_position)
            fuel += n * (n + 1) / 2

            # the following solution was 900 times slower...
            # fuel += sum(range(abs(crab - reference_position) + 1))

    return fuel


def calculate_lowest_fuel_with_mod_increase(horizontal_positions: list):
    """ Numeric solution of finding the median, returns a tuple of fuel used for optimal position """

    fuels = []
    for position in range(min(horizontal_positions), max(horizontal_positions)):
        fuels.append((calculate_fuel_for_point(horizontal_positions, position, mod_increase=True), position))

    return min(fuels)


if __name__ == "__main__":
    start = timeit.default_timer()

    with open('inputfiles/day7.txt', "r") as f:
        horizontal_positions = list(map(lambda x: int(x), f.read().split(",")))

    print(f"Solution Part I: {calculate_fuel_for_point(horizontal_positions, median(horizontal_positions))}")
    print(f"Solution Part II: {calculate_lowest_fuel_with_mod_increase(horizontal_positions)}")
    stop = timeit.default_timer()

    print(f"Took {stop - start} seconds to finish\n")

    # Part I:                            340987
    # Part II:                         96987874
    # All together:     Took 0.1668858340708539 seconds to finish

