# Advent of Code 2021
# Day 3: Part I + II

import timeit

with open('inputfiles/day3.txt', "r") as f:
    data = f.read().splitlines()


def part1_solved_on_string_base():
    """ first part of puzzle """
    count_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gamma_rate = ""
    epsilon_rate = ""

    for number_string in data:
        for position, digit in enumerate(number_string):
            if digit == "1":
                count_ones[position] += 1

    for count in count_ones:
        if count > len(data) / 2:   # more than half of the numbers have digit 1 here
            gamma_rate += "1"
            epsilon_rate += "0"
        else:                       # here more of them are digit 0
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)



def part2():
    """ second part of puzzle"""


if __name__ == "__main__":
    start = timeit.default_timer()
    print(part1_solved_on_string_base())
    part2()
    stop = timeit.default_timer()

    print(f"\nTook {stop - start} seconds to finish")

    # Part I: 1071734 - Took 0.0006397090037353337 seconds to finish



