# Advent of Code 2021
# Day 9: Part I

import timeit
from math import prod


def find_low_points(heat_map: list):
    """ finds any numbers which don't have higher numbers adjacent
        returns a list of index tuples for heat_map --> (row, position)
    """

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

            low_points.append((row, position))

    return low_points


def calculate_risk_level(low_points: list):
    """ return risk level based on found low points """
    return sum([heat_map[row][position] + 1 for row, position in low_points])


def find_basins(low_points, heat_map):
    """ for each low points seek all adjacent plus-one-numbers """
    basin_members_set = set()
    basins = []

    def seek_basin_members(position_tuple: tuple):
        """ inner function that runs while this_basin_temp_list is not empty. Each run it pops one off the list
            but also adds any new fount adjacent plus-one-number
            (checks left, above, right and under of each position)

            returns basin_set for given low number
        """
        this_basin_set = set()
        this_basin_set.add(position_tuple)

        this_basin_temp_list = [position_tuple]     # start with low_point

        while this_basin_temp_list:
            row, position = this_basin_temp_list.pop()

            # left
            if not position == 0:
                if heat_map[row][position - 1] == heat_map[row][position] + 1 \
                        and not heat_map[row][position - 1] == 9 \
                        and (row, position - 1) not in basin_members_set:
                    basin_members_set.add((row, position - 1))
                    this_basin_set.add((row, position - 1))
                    this_basin_temp_list.append((row, position - 1))

            # above
            if not row == 0:
                if heat_map[row - 1][position] == heat_map[row][position] + 1 \
                        and not heat_map[row - 1][position] == 9 \
                        and (row - 1, position) not in basin_members_set:
                    basin_members_set.add((row - 1, position))
                    this_basin_set.add((row - 1, position))
                    this_basin_temp_list.append((row - 1, position))

            # right
            if not position == (len(heat_map[0]) - 1):
                if heat_map[row][position + 1] == heat_map[row][position] + 1 \
                        and not heat_map[row][position + 1] == 9 \
                        and (row, position + 1) not in basin_members_set:
                    basin_members_set.add((row, position + 1))
                    this_basin_set.add((row, position + 1))
                    this_basin_temp_list.append((row, position + 1))

            # under
            if not row == (len(heat_map) - 1):
                if heat_map[row + 1][position] == heat_map[row][position] + 1 \
                        and not heat_map[row + 1][position] == 9 \
                        and (row + 1, position) not in basin_members_set:
                    basin_members_set.add((row + 1, position))
                    this_basin_set.add((row + 1, position))
                    this_basin_temp_list.append((row + 1, position))

        return this_basin_set

    for position_tuple in low_points:
        basins.append(seek_basin_members(position_tuple))

    return basins


if __name__ == "__main__":
    start = timeit.default_timer()
    with open('inputfiles/day9.txt', "r") as f:
        heat_map = [[int(x) for x in line.strip()] for line in f.read().splitlines()]

    # Part I
    low_points = find_low_points(heat_map)
    print(f"Part I: Risk level is {calculate_risk_level(low_points)}")

    # Part II
    basins = find_basins(low_points, heat_map)
    product_of_three_larges_basins = prod([len(basin) for basin in sorted(basins, key=len, reverse=True)[0:3]])
    print(f"Part II: Product of three largest basins ist {product_of_three_larges_basins}")


    stop = timeit.default_timer()

    print(f"Took {stop - start} seconds to finish\n")

    # Part I:                                 631
    # Part II:                             261568 - not the right result...
    # All together:     Took 0.007129625068046153 seconds to finish
