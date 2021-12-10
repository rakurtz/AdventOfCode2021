# Advent of Code 2021
# Day 5: Part I + II
import timeit


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

        if x1 == x2:
            # take care: in my_map y is the first index and x is the second!!
            if y1 < y2:
                for y_coordinate in range(abs(y1 - y2) + 1):
                    my_map[y1 + y_coordinate][x1] += 1
            else:
                for y_coordinate in range(abs(y1 - y2) + 1):
                    my_map[y1 - y_coordinate][x1] += 1

        elif y1 == y2:
            if x1 < x2:
                for x_coordinate in range(abs(x1 - x2) + 1):
                    my_map[y1][x1 + x_coordinate] += 1
            else:
                for x_coordinate in range(abs(x1 - x2) + 1):
                    my_map[y1][x1 - x_coordinate] += 1


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
    print(f"Part 1: There are {result} points of crossing lines")
    print(f"\nTook {stop - start} seconds to finish")

    # Part 1 = 7085 - Took 0.0987210419261828 seconds to finish

