# Advent of Code 2021
# Day 9: Part I

import timeit


def find_low_points(heat_map: list):
    """ finds any numbers which don't have higher numbers adjacent"""

    low_points = []
    for row, values in enumerate(heat_map):
        for position, value in enumerate(values):
            # compare each number to their neighbours, if found higher one (or equal one!), continue to next value

            # left
            if not position == 0:
                if heat_map[row][position - 1] <= value:
                    continue

            # above
            if not row == 0:
                if heat_map[row - 1][position] <= value:
                    continue

            # right
            if not position == (len(heat_map[0]) - 1):
                if heat_map[row][position + 1] <= value:
                    continue

            # under
            if not row == (len(heat_map) -1):
                if heat_map[row + 1][position] <= value:
                    continue

            low_points.append(value)

    return low_points


def calculate_risk_level(low_points: list):
    """ return risk level based on found low points """
    return sum([x + 1 for x in low_points])


if __name__ == "__main__":
    start = timeit.default_timer()
    with open('inputfiles/day9.txt', "r") as f:
        heat_map = [[int(x) for x in line.strip()] for line in f.read().splitlines()]

    low_points = find_low_points(heat_map)
    print(low_points)
    print(f"Part I: Risk level is {calculate_risk_level(low_points)}")

    stop = timeit.default_timer()

    print(f"Took {stop - start} seconds to finish\n")

    # Part I:                               631
    # Part II:                                0
    # All together:     Took 0.002446250058710575 seconds to finish
