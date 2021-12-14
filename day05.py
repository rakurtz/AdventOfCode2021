# Advent of Code 2021
# Day 5: Part I + II
import timeit
from pprint import pprint

def create_map_of_zeros(size: int):
    """ creates a map of 1000 x 1000 filled with zeros """
    this_map = []
    for x in range(size):
        this_map.append(0)
        this_map[x] = []
        for y in range(size):
            this_map[x].append(0)
    return this_map


def calculate_line_points(data):
    """ calculates all points of a line in data and adds them to my_map list"""
    global my_map
    for line in data:
        start_point, end_point = line.split("->")
        x1, y1 = map(lambda coordinate: int(coordinate), start_point.split(","))
        x2, y2 = map(lambda coordinate: int(coordinate), end_point.split(","))

        if y1 == y2:
            # vertical lines
            if x1 < x2:
                for x_step in range(abs(x1 - x2) + 1):
                    my_map[y1][x1 + x_step] += 1
            else:
                for x_step in range(abs(x1 - x2) + 1):
                    my_map[y1][x1 - x_step] += 1

        elif x1 == x2:
            # horizontal lines
            if y1 < y2:
                for y_step in range(abs(y1 - y2) + 1):
                    my_map[y1 + y_step][x1] += 1
            else:
                for y_step in range(abs(y1 - y2) + 1):
                    my_map[y1 - y_step][x1] += 1

        elif abs(y1 - y2) == abs(x1 - x2):
            # diagonal lines
            # north east
            if x2 > x1 and y2 < y1:
                for step in range(abs(y1 - y2) + 1):
                    my_map[y1 - step][x1 + step] += 1

            # south east
            if x2 > x1 and y2 > y1:
                for step in range(abs(y1 - y2) + 1):
                    my_map[y1 + step][x1 + step] += 1

            # south west
            if x2 < x1 and y2 > y1:
                for step in range(abs(y1 - y2) + 1):
                    my_map[y1 + step][x1 - step] += 1

            # north west
            if x2 < x1 and y2 < y1:
                for step in range(abs(y1 - y2) + 1):
                    my_map[y1 - step][x1 - step] += 1




def count_cross_line_points():
    """ return the number of points where lines cross """
    counter = 0
    for y in range(len(my_map)):
        for x in range(len(my_map[0])):
            if my_map[y][x] >= 2:
                counter += 1

    return counter


if __name__ == "__main__":
    start = timeit.default_timer()

    with open('inputfiles/day5.txt', "r") as f:
        data = f.read().splitlines()

    my_map = create_map_of_zeros(1000)  # is a global...
    calculate_line_points(data)
    result = count_cross_line_points()

    stop = timeit.default_timer()

    # The result...
    #pprint([[f"{number}" if number >= 1 else "." for number in line] for line in my_map])

    print(f"Part 1: There are {result} points of crossing lines")
    print(f"\nTook {stop - start} seconds to finish")

    # Part 1 =  7085 - Took 0.0987210419261828 seconds to finish
    # Part 2 = 20271 - Took 0.10050841700285673 seconds to finish

