# Advent of Code 2021
# Day 6: Part I

import timeit


def read_starting_population():
    global data
    global population
    for fish in data:
        population[fish] += 1


def populate_another_day():
    """ calculates another day for all fish"""
    global population

    # move population to the right and add new fish at the end...
    population = population[1:] + [population[0]]
    population[6] += population[8]


if __name__ == "__main__":
    start = timeit.default_timer()

    with open('inputfiles/day6.txt', "r") as f:
        data = f.read().split(",")
    data = map((lambda x: int(x)), data)

    population = [0] * 9  # each index represents the number of fish with there respektive days left
    read_starting_population()

    for _ in range(256):
        populate_another_day()

    stop = timeit.default_timer()

    print(f"Part 1: {sum(population)}")
    print(f"\nTook {stop - start} seconds to finish")

    # Part 1: 387413        - Took 0.00011954200454056263 seconds to finish
    # Part 2: 1738377086345 - Took 0.00017133296933025122 seconds to finish

