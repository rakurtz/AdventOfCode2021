# Advent of Code 2021
# Day 6: Part I

import timeit


def read_starting_population(data):
    global population
    for fish in data:
        population[fish] += 1


def populate_another_day():
    """ calculates another day for all fish"""
    global population
    d0, d1, d2, d3, d4, d5, d6, d7, d8 = population

    population = [d1, d2, d3, d4, d5, d6, d7, d8, d0]   # "move" each to the left and add d0 as new fish
    population[6] += d0                                 # re-add d0 fish at day 6


if __name__ == "__main__":
    start = timeit.default_timer()

    with open('inputfiles/day6.txt', "r") as f:
        data = f.read().split(",")
    data = map((lambda x: int(x)), data)

    population = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # each index represents the number of fish with there respektive days left

    read_starting_population(data)

    for _ in range(80):
        populate_another_day()

    stop = timeit.default_timer()
    print(f"Part 1: {sum(population)}")
    print(f"\nTook {stop - start} seconds to finish")

    # Part 1: 387413 - Took 0.00011954200454056263 seconds to finish

