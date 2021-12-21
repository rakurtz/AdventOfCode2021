# Advent of Code 2021
# Day 11: Part I

import timeit
from pprint import pprint


def on_flash_increase_adjacent(y, x):
    """
    takes a position x, y and increases the adjacent numbers in data by 1
    returns nothing
    """
    global data

    n = (y + 1, x)
    ne = (y + 1, x + 1)
    e = (y, x + 1)
    se = (y - 1, x + 1)
    s = (y - 1, x)
    sw = (y - 1, x - 1)
    w = (y, x - 1)
    nw = (y + 1, x - 1)

    all_positions = [n, ne, e, se, s, sw, w, nw]

    for position in all_positions:
        pos_y, pos_x = position
        try:
            data[pos_y][pos_x] += 1
        except IndexError:
            continue


def increase_all():
    global data
    data = [[i + 1 for i in row] for row in data]


def flash():
    global data
    global global_flash_counter
    global already_flashed

    flashed_someone = False

    for y, row in enumerate(data):
        for x, number in enumerate(row):
            if number > 9 and not [y, x] in already_flashed:
                already_flashed.append([y, x])
                global_flash_counter += 1
                on_flash_increase_adjacent(y, x)
                flashed_someone = True

    return flashed_someone


def repeated_flash():
    """ caller for flash()
        runs flash repeatedly until there's no other flashing
    """
    while True:
        if not flash():
            break


def printer(mode="string"):
    """ prints data as in sample in AoC """
    #mode = "pprint"
    if mode == "string":
        for row in data:
            print(''.join([str(i) for i in row]))
        print("\n")
    else:
        pprint(data)

    print()


def reset_flashed():
    global data

    for flashed in already_flashed:
        y, x = flashed
        data[y][x] = 0


if __name__ == "__main__":
    start = timeit.default_timer()

    with open('inputfiles/day11.txt', "r") as f:
        data = f.read().splitlines()

    data = [[int(i) for i in line] for line in data]
    global_flash_counter = 0

    #printer()

    for _ in range(100):
        already_flashed = []

        increase_all()
        repeated_flash()
        reset_flashed()

        #printer()

    print(global_flash_counter, "\n")
    stop = timeit.default_timer()

    print(f"Took {stop - start} seconds to finish\n")
    # unfortunately this returns no correct result. After step 2 the numbers start to differ.
    # don't know why...

